from loader import extract_parameter_set, ParameterSet
from parse_metaprompt import parse_metaprompt, extract_tokens


def extract_variables(ast):
    return extract_parameter_set(ast).required


def test_extractor_1():
    prompt = """
    [:foo]
    """
    assert extract_variables(parse_metaprompt(prompt)) == set(["foo"])


def test_extractor_2():
    prompt = """
    [:foo][:bar]
    """
    assert extract_variables(parse_metaprompt(prompt)) == set(["foo", "bar"])


def test_extractor_assign_1():
    prompt = """
    [:foo=baz][:bar]
    """
    assert extract_variables(parse_metaprompt(prompt)) == set(["bar"])


def test_extractor_assign_2():
    prompt = """
    [:foo=baz][:foo]
    """
    assert extract_variables(parse_metaprompt(prompt)) == set()


def test_extractor_assign_3():
    prompt = """
    [:foo][:foo=baz] - first used, then assigned
    """
    assert extract_variables(parse_metaprompt(prompt)) == set(["foo"])


def test_extractor_assign_4():
    prompt = """
    [:foo][:foo=baz] - first used, then assigned
    """
    assert extract_variables(parse_metaprompt(prompt)) == set(["foo"])


def test_extractor_assign_5():
    prompt = """
    [:foo][:foo=baz] - first used, then assigned
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set(["foo"])
    assert res.optional == set()
    assert res.assigned == set(["foo"])


def test_extractor_assign_6():
    prompt = """
    [:foo?=default]
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set()
    assert res.optional == set(["foo"])
    assert res.assigned == set(["foo"])


def test_extractor_if():
    prompt = """
    [:if [:foo=bar] :then [:foo] :else [:foo]]
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set()
    assert res.optional == set()
    assert res.assigned == set(["foo"])


def test_extractor_if_single_branch_assign():
    prompt = """
    [:if ... :then [:foo=bar] :else [:foo]]
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set(["foo"])
    assert res.optional == set()
    assert res.assigned == set()


def test_extractor_if_both_branches_assign():
    prompt = """
    [:if ... :then [:foo=bar] :else [:foo=baz]]
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set()
    assert res.optional == set()
    assert res.assigned == set(["foo"])


def test_extractor_if_both_branches_require():
    prompt = """
    [:if ... :then [:foo] :else [:foo]]
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set(["foo"])
    assert res.optional == set()
    assert res.assigned == set()


def test_extractor_if_single_branch_requires():
    prompt = """
    [:if ... :then [:foo] :else ...]
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set(["foo"])
    assert res.optional == set()
    assert res.assigned == set()

    prompt = """
    [:if ... :then ... :else [:foo]]
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set(["foo"])
    assert res.optional == set()
    assert res.assigned == set()


def test_extractor_if_single_branch_optionally_assigns():
    prompt = """
    [:if ... :then [:foo?=bar] :else ...]
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set()
    assert res.optional == set(["foo"])
    assert res.assigned == set()


def test_extractor_if_both_branches_assign_var():
    prompt = """
    [:if ... :then [:foo=bar] :else [:foo=bar]][:foo]
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set()
    assert res.optional == set()
    assert res.assigned == set(["foo"])


def test_extractor_if_single_branch_assigns_var():
    prompt = """
    [:if ... :then [:foo=bar] :else ...][:foo] <- required
    """
    res = extract_parameter_set(parse_metaprompt(prompt))
    assert res.required == set(["foo"])
    assert res.optional == set()
    assert res.assigned == set()
