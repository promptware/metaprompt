from config import Config
from env import Env
from runtime import BaseRuntime
from typing import AsyncGenerator, List
from loader import extract_parameter_set
from eval_utils.assignment import Assignment
from eval_utils.chat_history import serialize_chat_history

IF_PROMPT = """Please determine if the following statement is true.
Do not write any other output, answer just "true" or "false".
The statement:
"""

ALLOWED_ROLES = ["system", "user", "assistant"]


async def eval_ast(ast, config, runtime):
    env = Env(**config.parameters)
    chats = dict()
    default_model = config.providers.get_default_model()
    if default_model is not None:
        env.set("MODEL", default_model.strip())

    def get_model():
        nonlocal env
        if env.get("MODEL") is None:
            raise ValueError(
                "Default model was not specified. ProviderConfig must have at least one provider"
            )
        return env.get("MODEL").strip()

    async def _eval_exprs(exprs):
        """A helper for eval_ast"""
        for expr in exprs:
            async for chunk in _eval_ast(expr):
                yield chunk

    async def _collect_exprs(exprs):
        """_eval_ast, but returns everything as text"""
        res = ""
        for expr in exprs:
            async for chunk in _eval_ast(expr):
                res += chunk
        return res

    def get_current_model_provider():
        nonlocal env
        model_name = get_model()
        provider = config.providers.get(model_name)
        if provider is None:
            raise ValueError(f"Model not available: {model_name}")
        return provider

    async def stream_invoke(
        chat: List[{"role": str, "content": str}],
        history: List[{"role": str, "content": str}] = [],
    ) -> AsyncGenerator[str, None]:
        provider = get_current_model_provider()
        async for chunk in provider.ainvoke(chat, history):
            yield chunk

    async def invoke(chat, history) -> str:
        res = ""
        async for chunk in stream_invoke(chat, history):
            res += chunk
        return res

    async def _eval_ast(ast):
        nonlocal env, runtime, chats
        if isinstance(ast, list):
            # TODO: is this case needed?
            async for chunk in _eval_exprs(ast):
                yield chunk
        elif ast["type"] == "text":
            yield ast["text"]
        elif ast["type"] == "metaprompt":
            async for chunk in _eval_exprs(ast["exprs"]):
                yield chunk
        elif ast["type"] == "var":
            value = env.get(ast["name"])
            if value is None:
                raise ValueError(f"Failed to look up: {ast['name']}")
            else:
                yield value
        elif ast["type"] == "use":
            parameters = ast["parameters"]
            module_name = ast["module_name"]
            loaded_ast = runtime.load_module(module_name)
            required_variables = extract_parameter_set(loaded_ast).required
            for required in required_variables:
                if required not in parameters:
                    raise ImportError(
                        f"Module {module_name} requires {required} as a parameter, but it was not provided"
                    )
            # TODO: persist some variables?
            evaluated_parameters = {}
            for parameter in parameters:
                evaluated_parameters[parameter] = await _collect_exprs(
                    parameters[parameter]
                )
            # save parent state in a closure
            old_env = env
            old_chats = chats
            # prepare new state
            if "MODEL" not in evaluated_parameters:
                evaluated_parameters["MODEL"] = get_model()
            env = Env(evaluated_parameters)
            chats = {}
            # recurse
            async for chunk in _eval_ast(loaded_ast):
                yield chunk
            # restore parent state
            env = old_env
            chats = old_chats
            if "STATUS" in old_env:
                runtime.set_status(old_env["STATUS"])
        elif ast["type"] == "assign":
            var_name = ast["name"]
            value = (await _collect_exprs(ast["exprs"])).strip()
            if ast["required"] or env.get(var_name) is None:
                if var_name == "STATUS":
                    runtime.set_status(value)
                elif var_name == "ROLE":
                    if value not in ALLOWED_ROLES:
                        raise ValueError(
                            "ROLE variable must be one of "
                            + "".join([f"'{role}', " for role in ALLOWED_ROLES])
                            + ", you specified: "
                            + value
                        )
                    yield Assignment("ROLE", value)
                env.set(var_name, value)
        elif ast["type"] == "meta":
            # Load chat history
            chat_id = ast["chat"] if "chat" in ast else None
            if chat_id is not None:
                if chat_id not in chats:
                    chats[chat_id] = []
            # evaluate the prompt messages
            messages = []
            current_message = ""
            current_role = env.get("ROLE") or "user"  # TODO: default role?
            for expr in ast["exprs"]:
                async for chunk in _eval_ast(expr):
                    if isinstance(chunk, Assignment) and chunk.name == "ROLE":
                        # TODO: strip in a more generic fashion
                        if len(current_message.strip()) > 0:
                            messages.append(
                                {
                                    "role": current_role,
                                    "content": current_message,
                                }
                            )
                        current_message = ""
                        current_role = chunk.value
                    else:
                        current_message += chunk
            if len(current_message.strip()) > 0:
                messages.append(
                    {"role": current_role, "content": current_message}
                )
            # collect the assistant response
            assistant_response = ""
            async for chunk in stream_invoke(
                messages, chats[chat_id] if chat_id in chats else []
            ):
                assistant_response += chunk
                yield chunk
            # update chat history
            if chat_id is not None:
                chats[chat_id].extend(messages)
                chats[chat_id].append(
                    {"role": "assistant", "content": assistant_response}
                )
                env.set(chat_id, serialize_chat_history(chats[chat_id]))
        elif ast["type"] == "exprs":
            for expr in ast["exprs"]:
                async for chunk in _eval_ast(expr):
                    yield chunk
        elif ast["type"] == "if_then_else":
            # evaluate the conditional
            condition = await _collect_exprs(ast["condition"])
            condition = condition.strip()
            # short-curcuit the evaluation: if the condition text is literally
            # 'true' or 'false', then use it to dispatch into the :if branch.
            # That way we can use FFI functions with :if statements
            prompt_result = (
                "" if condition not in ["false", "true"] else condition
            )
            MAX_RETRIES = 3  # TODO: move to config
            retries = 0
            prompt = IF_PROMPT + condition
            while prompt_result != "true" and prompt_result != "false":
                if retries >= MAX_RETRIES:
                    raise ValueError(
                        "Failed to answer :if prompt: "
                        + prompt
                        + "\nOutput: "
                        + prompt_result
                    )
                prompt_result = await invoke(
                    [
                        {"role": "system", "content": IF_PROMPT},
                        {"role": "user", "content": condition},
                    ],
                    [],
                )
                prompt_result = prompt_result.strip()
                retries += 1
            if prompt_result == "true":
                async for chunk in _eval_ast(ast["then"]):
                    yield chunk
            else:  # false
                async for chunk in _eval_ast(ast["else"]):
                    yield chunk
        else:
            raise ValueError("Runtime AST evaluation error: " + str(ast))

    async for chunk in _eval_ast(ast):
        yield chunk


async def stream_eval_metaprompt(
    metaprompt, config: Config, runtime: BaseRuntime
) -> AsyncGenerator[str, None]:
    async for chunk in eval_ast(metaprompt, config, runtime):
        yield chunk


async def eval_metaprompt(metaprompt, config: Config, runtime: BaseRuntime):
    res = ""
    async for chunk in stream_eval_metaprompt(metaprompt, config, runtime):
        res += chunk
    return res
