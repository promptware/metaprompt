from metaprompt import metaprompt
from config import Config
from providers.mock import MockProvider
from runtimes.mock import MockRuntime

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
async def test_if_4():
    prompt = """
    [:if test :then foo :else bar]
"""
    result = await metaprompt(
        prompt,
        Config(
            providers=MockProvider(
                rules=[
                    (
                        {"chat": r"test"},
                        "true",
                    ),
                ]
            )
        ),
    )

    expected = "foo"
    assert result.strip() == expected.strip()


@pytest.mark.asyncio
async def test_if_5():
    prompt = """
    [:if test :then foo :else bar]
"""
    result = await metaprompt(
        prompt,
        Config(
            providers=MockProvider(
                rules=[
                    (
                        {"chat": r"test"},
                        "false",
                    ),
                ]
            )
        ),
    )

    expected = "bar"
    assert result.strip() == expected.strip()


@pytest.mark.asyncio
async def test_model_switch():
    prompt = """
    [$ whoami][:MODEL=mock2][$ whoami ][:MODEL=mock1][$ whoami ]
"""
    result = await metaprompt(
        prompt,
        Config(
            model="mock1",
            providers=MockProvider(
                models=["mock1"],
                rules=[
                    (
                        {"chat": r"whoami"},
                        "mock1",
                    ),
                ],
            ).merge(
                MockProvider(
                    models=["mock2"],
                    rules=[
                        (
                            {"chat": r"whoami"},
                            "mock2",
                        ),
                    ],
                )
            ),
        ),
    )

    expected = "mock1mock2mock1"
    assert result.strip() == expected.strip()


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
                        {"chat": r"is a car. remember this"},
                        "OK, remembered car",
                    ),
                    (
                        {"chat": r"is an apple. remember this"},
                        "OK, remembered apple",
                    ),
                    (
                        {"chat": r"ride. remember this"},
                        "OK, remembered ride",
                    ),
                    (
                        {"chat": r"eat. remember this"},
                        "OK, remembered eat",
                    ),
                    (
                        {
                            "chat": r"Combine",
                            "history": r"remembered apple",
                        },
                        "eat an apple",
                    ),
                    (
                        {
                            "chat": r"Combine",
                            "history": r"remembered car",
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


@pytest.mark.asyncio
async def test_counter():
    prompt = """
counter is: [:number]
[:if [:number] is zero or less
 :then done!
 :else [:use ./counter
    :number=[$ subtract one from [:number].
    just give me the resulting number, no other output]]
]"""
    result = await metaprompt(
        prompt,
        Config(
            providers=MockProvider(
                rules=[
                    ({"chat": r"3 is zero"}, "false"),
                    ({"chat": r"subtract one from 3"}, "2"),
                    ({"chat": r"2 is zero"}, "false"),
                    ({"chat": r"subtract one from 2"}, "1"),
                    ({"chat": r"1 is zero"}, "false"),
                    ({"chat": r"subtract one from 1"}, "0"),
                    ({"chat": r"0 is zero"}, "true"),
                ]
            ),
            parameters={"number": "3"},
        ),
        runtime=MockRuntime(
            modules={"./counter": prompt},
        ),
    )

    expected = """
counter is: 3

counter is: 2

counter is: 1

counter is: 0
 done!
"""
    assert result.strip() == expected.strip()
