from config import Config
from env import Env
from runtime import BaseRuntime
from typing import AsyncGenerator
from loader import extract_variables


IF_PROMPT = """Please determine if the following statement is true.
Do not write any other output, answer just "true" or "false".
The statement:
"""


async def eval_ast(ast, config, runtime):
    env = Env(**config.parameters)
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

    async def stream_invoke(prompt: str) -> AsyncGenerator[str, None]:
        provider = get_current_model_provider()
        async for chunk in provider.ainvoke(prompt, "user"):
            yield chunk

    async def invoke(self, prompt: str) -> str:
        res = ""
        async for chunk in self.stream_invoke(prompt):
            res += chunk
        return res

    async def _eval_ast(ast):
        nonlocal env, runtime
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
            required_variables = extract_variables(loaded_ast)
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
            old_env = env
            if "MODEL" not in evaluated_parameters:
                evaluated_parameters["MODEL"] = get_model()
            env = Env(evaluated_parameters)
            async for chunk in _eval_ast(loaded_ast):
                yield chunk
            env = old_env
        elif ast["type"] == "assign":
            var_name = ast["name"]
            value = (await _collect_exprs(ast["exprs"])).strip()
            if var_name == "STATUS":
                runtime.set_status(value)
            env.set(var_name, value)
        elif ast["type"] == "meta":
            chunks = []
            for expr in ast["exprs"]:
                async for chunk in _eval_ast(expr):
                    chunks.append(chunk)
            prompt = "".join(chunks)
            async for chunk in stream_invoke(prompt):
                yield chunk
        elif ast["type"] == "exprs":
            for expr in ast["exprs"]:
                async for chunk in _eval_ast(expr):
                    yield chunk
        elif ast["type"] == "if_then_else":
            # evaluate the conditional
            condition = await _collect_exprs(ast["condition"])
            prompt_result = ""
            MAX_RETRIES = 3
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
                prompt_result = (await invoke(prompt)).strip()
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
