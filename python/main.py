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
        openai_api_key=openai_api_key,
        temperature=0.7,
        model_name="gpt-3.5-turbo",
    )
    messages = [HumanMessage(content=prompt)]
    response = chat_model(messages)
    print(
        f"Prompt: {prompt}\nOutput: {response.content}\n-----------------------------"
    )
    return response.content


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


async def main():
    providers = [
        openai_provider(
            ["gpt-3.5-turbo"], openai_api_key=openai_api_key, temperature=0.7
        )
    ]
    prompt = """
    Write me a poem about [:subject]
    [:if [:subject] is a human
     :then Use jokingly exaggerated style
     :else
       Include some references to
       [$ List some people who have any relation to [:subject],
          comma-separated
       ]
    ]
    """
    ast = parse_metaprompt(prompt)
    config = Config(parameters={"subject": "Saint Petersburg"})
    res = await eval_metaprompt(ast, config)
    print(llm_input(res))


if __name__ == "__main__":
    asyncio.run(main())
