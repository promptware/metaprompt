from metaprompt import metaprompt
from config import Config
from providers.mock import MockProvider

import pytest
import re


@pytest.mark.asyncio
async def test_parameters():
    prompt = "[:foo][:foo]"
    assert (
        await metaprompt(prompt, Config(parameters={"foo": "bar"})) == "barbar"
    )


@pytest.mark.asyncio
async def test_assign1():
    prompt = "[:foo=bar][:foo][:foo]"
    assert await metaprompt(prompt) == "barbar"


@pytest.mark.asyncio
async def test_assign2():
    prompt = "[:foo=bar][:foo=[:foo][:foo]][:foo]"
    assert await metaprompt(prompt) == "barbar"


@pytest.mark.asyncio
async def test_if_1():
    prompt = "[:if false :then foo :else bar]"
    assert await metaprompt(prompt) == " bar"


@pytest.mark.asyncio
async def test_if_2():
    prompt = "[:if true :then foo :else bar]"
    assert await metaprompt(prompt) == " foo "


@pytest.mark.asyncio
async def test_if_3():
    prompt = "[:v1=tr][:v2=ue][:if [:v1][:v2] :then foo :else bar]"
    assert await metaprompt(prompt) == " foo "


@pytest.mark.asyncio
async def test_chat_history():
    prompt = """
[:_=[chat1$ the $OBJECT is a car. remember this]]
[:_=[chat2$ the $OBJECT is an apple. remember this]]
[:_=[chat1$ the $ACTION is ride. remember this]]
[:_=[chat2$ the $ACTION is eat. remember this]]
[:question=
  Combine the $ACTION and the $OBJECT
  into a single phrase. Give me just the phrase,
  no other output
]
chat1: [chat1$ [:question]]
chat2: [chat2$ [:question]]
"""
    result = await metaprompt(
        prompt,
        Config(
            providers=MockProvider(
                rules=[
                    (
                        {"chat": re.compile(r"is a car. remember this")},
                        "OK, remembered car",
                    ),
                    (
                        {"chat": re.compile(r"is an apple. remember this")},
                        "OK, remembered apple",
                    ),
                    (
                        {"chat": re.compile(r"ride. remember this")},
                        "OK, remembered ride",
                    ),
                    (
                        {"chat": re.compile(r"eat. remember this")},
                        "OK, remembered eat",
                    ),
                    (
                        {
                            "chat": re.compile(r"Combine"),
                            "history": re.compile(r"remembered apple"),
                        },
                        "eat an apple",
                    ),
                    (
                        {
                            "chat": re.compile(r"Combine"),
                            "history": re.compile(r"remembered car"),
                        },
                        "ride a car",
                    ),
                ]
            )
        ),
    )

    expected = """
chat1: ride a car
chat2: eat an apple
"""
    assert result.strip() == expected.strip()
