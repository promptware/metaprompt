from loader import extract_variables
from parse_metaprompt import parse_metaprompt, extract_tokens

def test_extractor_1():
    prompt="""
    [:foo]
    """
    assert extract_variables(parse_metaprompt(prompt)) == set(["foo"])


def test_extractor_2():
    prompt="""
    [:foo][:bar]
    """
    assert extract_variables(parse_metaprompt(prompt)) == set(["foo","bar"])


def test_extractor_assign_1():
    prompt="""
    [:foo=baz][:bar]
    """
    assert extract_variables(parse_metaprompt(prompt)) == set(["bar"])


def test_extractor_assign_2():
    prompt="""
    [:foo=baz][:foo]
    """
    assert extract_variables(parse_metaprompt(prompt)) == set()

def test_extractor_assign_3():
    prompt="""
    [:foo][:foo=baz] - first used, then assigned
    """
    assert extract_variables(parse_metaprompt(prompt)) == set(["foo"])
