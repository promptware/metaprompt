from parse_metaprompt import parse_metaprompt
import asyncio
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the OpenAI API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")


def llm_input(prompt):
    chat_model = ChatOpenAI(
        openai_api_key=openai_api_key, temperature=0.7, model_name="gpt-3.5-turbo"
    )
    messages = [HumanMessage(content=prompt)]
    response = chat_model(messages)
    print(f"Prompt: {prompt}\nOutput: {response}\n-----------------------------")
    return response.content


async def eval_exprs(exprs, runtime):
    for expr in exprs:
        async for chunk in eval_ast(expr, runtime):
            yield chunk


IF_PROMPT = """Please determine if the following statement is true.
Do not write any other output, answer just "true" or "false".
The statement:
"""


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
        output = llm_input("".join(chunks))
        yield output
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
            prompt_result = llm_input(prompt).strip()
            retries += 1
            if retries >= MAX_RETRIES:
                raise ValueError(
                    "Failed to answer :if prompt: " + prompt + "\nOutput: " + prompt_result
                )
        if prompt_result == "true":
            async for chunk in eval_ast(ast["then"], runtime):
                yield chunk
        else:  # false
            async for chunk in eval_ast(ast["else"], runtime):
                yield chunk
    else:
        raise ValueError("Runtime AST evaluation error: " + str(ast))


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
    # prompt = "[:asd]f[o]o[:asd][:if [:object] is a human :then hiii]"
    #    prompt = """
    #    Write me a poem about [:subject]

    # [:if [:subject] is a human
    #    :then
    #   Use jokingly exaggerated style
    # :else
    #   Include some references to [$ List some people who have any
    #   relation to [:subject], comma-separated
    #    ]
    #  ]
    #    """
    prompt = """
    """
    ast = parse_metaprompt(prompt)
    config = Config(parameters={"subject": "Saint Petersburg"})
    res = await eval_metaprompt(ast, config)
    print(llm_input(res))
    # print(ast)


if __name__ == "__main__":
    asyncio.run(main())
