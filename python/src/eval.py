from config import Config
from env import Env
from runtime import Runtime
from typing import AsyncGenerator
from loader import extract_variables

async def _eval_exprs(exprs, runtime):
    """A helper for eval_ast"""
    for expr in exprs:
        async for chunk in eval_ast(expr, runtime):
            yield chunk

async def _collect_exprs(exprs, runtime):
    res = ""
    for expr in exprs:
        async for chunk in eval_ast(expr, runtime):
            res += chunk
    return res


IF_PROMPT = """Please determine if the following statement is true.
Do not write any other output, answer just "true" or "false".
The statement:
"""


async def eval_ast(ast, runtime):
    if isinstance(ast, list):
        # TODO: is this case needed?
        async for expr in _eval_exprs(ast, runtime):
            yield expr
    elif ast["type"] == "text":
        yield ast["text"]
    elif ast["type"] == "metaprompt":
        async for expr in _eval_exprs(ast["exprs"], runtime):
            yield expr
    elif ast["type"] == "var":
        value = runtime.env.get(ast["name"])
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
        old_env = runtime.env
        # TODO: persist some variables?
        runtime.env = Env(parameters)
        async for expr in eval_ast(loaded_ast, runtime):
            yield expr
        runtime.env = old_env

    elif ast["type"] == "assign":
        var_name = ast["name"]
        value = await _collect_exprs(ast['exprs'], runtime)
        runtime.set_variable(var_name, value)
    elif ast["type"] == "meta":
        chunks = []
        for expr in ast["exprs"]:
            async for chunk in eval_ast(expr, runtime):
                chunks.append(chunk)
        prompt = "".join(chunks)
        async for chunk in runtime.stream_invoke(prompt):
            yield chunk
    elif ast["type"] == "exprs":
        for expr in ast["exprs"]:
            async for chunk in eval_ast(expr, runtime):
                yield chunk
    elif ast["type"] == "if_then_else":
        # evaluate the conditional
        condition_chunks = []
        async for chunk in eval_ast(ast["condition"], runtime):
            condition_chunks.append(chunk)
        condition = "".join(condition_chunks)
        prompt_result = ""
        MAX_RETRIES = 3
        retries = 0
        prompt = IF_PROMPT + condition
        while prompt_result != "true" and prompt_result != "false":
            prompt_result = await runtime.invoke(prompt)
            prompt_result = prompt_result.strip()
            retries += 1
            if retries >= MAX_RETRIES:
                raise ValueError(
                    "Failed to answer :if prompt: "
                    + prompt
                    + "\nOutput: "
                    + prompt_result
                )
        if prompt_result == "true":
            async for chunk in eval_ast(ast["then"], runtime):
                yield chunk
        else:  # false
            async for chunk in eval_ast(ast["else"], runtime):
                yield chunk
    else:
        raise ValueError("Runtime AST evaluation error: " + str(ast))


async def stream_eval_metaprompt(metaprompt, config: Config) -> AsyncGenerator[str, None]:
    env = Env(env=config.parameters)
    runtime = Runtime(config, env)
    async for chunk in eval_ast(metaprompt, runtime):
        yield chunk


async def eval_metaprompt(metaprompt, config: Config):
    res = ""
    async for chunk in stream_eval_metaprompt(metaprompt, config):
        res += chunk
    return res
