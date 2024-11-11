import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from config import Config
from providers.openai import OpenAIProvider
from metaprompt import stream_metaprompt

from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


prompt = """
[$
  Write me a poem about [:subject]
  [:if [:subject] is a human
   :then
     Use jokingly exaggerated style
   :else
     Include some references to
     [$ List some people who have any relation to [:subject],
       comma-separated
     ]
  ]
]
"""

async def main ():
    print("The metaprompt you are about to execute:")
    print(prompt)

    subject = input("What or who do you want to write a poem about: ")

    config = Config(
        providers = OpenAIProvider(api_key=openai_api_key),
        model = "gpt-3.5-turbo",
        parameters = { "subject": subject }
    )

    async for chunk in stream_metaprompt(prompt, config):
        print(chunk, end='')

if __name__ == '__main__':
    asyncio.run(main())
