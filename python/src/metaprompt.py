from config import Config
from eval import eval_metaprompt, stream_eval_metaprompt
from parse_metaprompt import parse_metaprompt
from runtime import BaseRuntime
from runtimes.cli_runtime import CliRuntime


async def metaprompt(
    prompt: str, config: Config = Config(), runtime: BaseRuntime = None
):
    if runtime is None:
        runtime = CliRuntime()
    ast = parse_metaprompt(prompt)
    res = await eval_metaprompt(ast, config, runtime)
    return res


async def stream_metaprompt(
    prompt: str, config: Config, runtime: BaseRuntime = None
):
    if runtime is None:
        runtime = CliRuntime()
    ast = parse_metaprompt(prompt)
    async for chunk in stream_eval_metaprompt(ast, config, runtime):
        yield chunk
