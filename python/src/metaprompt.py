from config import Config
from eval import eval_metaprompt, stream_eval_metaprompt
from parse_metaprompt import parse_metaprompt


async def metaprompt(prompt: str, config: Config):
    ast = parse_metaprompt(prompt)
    res = await eval_metaprompt(ast, config)
    return res

async def stream_metaprompt(prompt: str, config: Config):
    ast = parse_metaprompt(prompt)
    async for chunk in stream_eval_metaprompt(ast, config):
        yield chunk
