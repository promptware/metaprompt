import sys
from pprint import pprint
from antlr4 import *
from python_gen.src.MetaPromptLexer import MetaPromptLexer
from python_gen.src.MetaPromptParser import MetaPromptParser
from python_gen.src.MetaPromptVisitor import MetaPromptVisitor
from antlr4.error.ErrorListener import ErrorListener
from parser import parse_ast
import asyncio


async def eval_exprs(exprs, runtime):
    for expr in exprs:
        async for chunk in eval_ast(expr, runtime):
            yield chunk


async def eval_ast(ast, runtime):
    if isinstance(ast, list):
        async for expr in eval_exprs(ast, runtime):
            yield expr
    elif ast["type"] == "text":
        yield ast["text"]
    elif ast["type"] == "metaprompt":
        async for expr in eval_exprs(ast["exprs"], runtime):
            yield expr
    elif ast["type"] == "var":
        value = runtime.env.get(ast["name"])
        if value is None:
            raise ValueError(f"Failed to look up: {ast['name']}")
        else:
            yield value
    elif ast["type"] == "meta":
        chunks = []
        for expr in ast["exprs"]:
            async for chunk in eval_ast(expr, runtime):
                chunks.append(chunk)
        output = input("[$ " + "".join(chunks) + "]")
        yield output
    elif ast["type"] == "brackets":
        yield "["
        for expr in ast["exprs"]:
            async for chunk in eval_ast(expr, runtime):
                yield chunk
        yield "]"
    elif ast["type"] == "meta":
        chunks = []
        for expr in ast["exprs"]:
            async for chunk in eval_ast(expr, runtime):
                chunks.append(chunk)
        output = input("[$ " + "".join(chunks) + "]")
        yield output
    elif ast["type"] == "if_then":
        # evaluate the conditional
        condition_chunks = []
        async for chunk in eval_ast(ast["condition"], runtime):
            condition_chunks.append(chunk)
        condition = "".join(condition_chunks)
        #
        prompt_result = ""
        while prompt_result != "yes" and prompt_result != "no":
            prompt_result = input("yes or no: " + condition)
        if prompt_result == "yes":
            async for chunk in eval_ast(ast["then"], runtime):
                yield chunk
        else:
            if "else" in ast:
                async for chunk in eval_ast(ast["else"], runtime):
                    yield chunk
            else:
                pass
    else:
        raise ValueError(ast)


async def eval_metaprompt(metaprompt, config):
    env = Env(env=config.parameters)
    runtime = Runtime(config, env)
    res = ""
    async for chunk in eval_ast(metaprompt, runtime):
        res += chunk
    return res


class Provider:
    def __init__(self):
        pass

    def does_support_model(self, model):
        return False

    async def eval_prompt(self, model, prompt):
        pass


class InteractiveCliProvider(Provider):
    def __init__(self):
        pass

    def does_support_model(self, model):
        return model == "interactive"

    async def eval_prompt(self, model, prompt):
        if model == "interactive":
            res = input(prompt)
            return res
        raise ValueError(f"Model not supported: {model}")


class Config:

    def __init__(self, parameters):
        self.parameters = parameters
        self.if_retries = 3

    def meta_eval(self, prompt):
        pass


class Env:

    def __init__(self, env={}, parent=None):
        self.env = env
        self.parent = parent

    def set(self, variable, value):
        self.env[variable] = value

    def get(self, variable):
        if variable in self.env:
            return self.env[variable]
        elif self.parent is not None:
            self.parent.lookup(variable)
        else:
            return None


class Runtime:
    def __init__(self, config, env):
        self.config = config
        self.env = env


async def main():
    # prompt = 'as[d] [:if foo asd :then] [:hi] [:if [:foo] is a [:if c2 :then then2] human :then bar :else baz]'
    prompt = "[:asd]f[o]o[:asd][:if [:object] is an animal :then hiii]"
    ast = parse_ast(prompt)
    pprint(ast, indent=2)
    config = Config(parameters={"asd": "hello", "object": "man"})
    res = await eval_metaprompt(ast, config)
    print(res)
    # print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    asyncio.run(main())
