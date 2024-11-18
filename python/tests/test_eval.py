import pytest
from metaprompt import metaprompt
from config import Config


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
