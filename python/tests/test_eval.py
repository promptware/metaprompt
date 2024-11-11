import pytest
from metaprompt import metaprompt
from config import Config

@pytest.mark.asyncio
async def test_parameters():
    prompt = "[:foo][:foo]"
    await metaprompt(
        prompt,
        Config(
            parameters = {
                'foo': 'bar'
            }
        )
    ) == "barbar"


@pytest.mark.asyncio
async def test_assign1():
    prompt = "[:foo=bar][:foo][:foo]"
    await metaprompt(
        prompt
    ) == "barbar"


@pytest.mark.asyncio
async def test_assign2():
    prompt = "[:foo=bar][:foo=[:foo][:foo]][:foo]"
    await metaprompt(
        prompt
    ) == "barbar"
