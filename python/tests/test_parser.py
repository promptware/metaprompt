from parse_metaprompt import (
    parse_metaprompt,
    extract_tokens,
)
from parse_utils import remove_extra_whitespace


def t(text):
    return {"type": "text", "text": text}


def comment(exprs):
    return {"type": "comment", "exprs": exprs}


def if_then(c, then_):
    return if_then_else(c, then_, [])


def if_then_else(c, then_, else_):
    return {
        "type": "if_then_else",
        "condition": c,
        "then": then_,
        "else": else_,
    }


def meta(exprs, chat_id=None):
    if chat_id is None:
        return {"type": "meta", "exprs": exprs}
    else:
        return {"type": "meta", "exprs": exprs, "chat": chat_id}


def var(name):
    return {"name": name, "type": "var"}


def use(module_name, parameters):
    return {"type": "use", "module_name": module_name, "parameters": parameters}


def assign(name, exprs, required=True):
    return {
        "type": "assign",
        "required": required,
        "name": name,
        "exprs": exprs,
    }


def choose(criterion, options, default):
    return {
        "criterion": criterion,
        "options": options,
        "default": default,
        "type": "choose",
    }


def option(option, description):
    return {"option": option, "description": description}


def call(name, pos_args, named_args):
    return {
        "type": "call",
        "name": name,
        "positional_args": pos_args,
        "named_args": named_args,
    }


def test_empty():
    result = parse_metaprompt("")
    assert result["exprs"] == []


def test_text_0():
    result = parse_metaprompt("asd")
    assert result["exprs"] == [{"text": "asd", "type": "text"}]


def test_text_1():
    result = parse_metaprompt("$$")
    assert result["exprs"] == [t("$$")]


def test_text_2():
    result = parse_metaprompt("$=")
    assert result["exprs"] == [t("$=")]


def test_text_kw_is():
    result = parse_metaprompt(":is")
    assert result["exprs"] == [t(":is")]


def test_escaping():
    result = parse_metaprompt("\\")
    assert result["exprs"] == [t("\\")]


def test_escaping_1():
    result = parse_metaprompt("\\[")
    assert result["exprs"] == [t("[")]


def test_escaping_2():
    result = parse_metaprompt("\\[:foo]")
    assert result["exprs"] == [t("[:foo]")]


def test_escaping_2_1():
    result = parse_metaprompt("\\\\[:foo]")
    assert result["exprs"] == [t("\\\\"), var("foo")]


def test_escaping_2_2():
    result = parse_metaprompt("\\\\")
    assert result["exprs"] == [t("\\\\")]


def test_escaping_3():
    result = parse_metaprompt("\\[:foo")
    assert result["exprs"] == [t("[:foo")]


def test_escaping_4():
    result = parse_metaprompt("\\\\[")
    assert result["exprs"] == [t("\\\\[")]


def test_escaping_5():
    result = parse_metaprompt("\\  \\")
    assert result["exprs"] == [t("\\  \\")]


def test_comment():
    result = parse_metaprompt("[# asd ]")
    assert result["exprs"] == [comment([{"text": " asd ", "type": "text"}])]


def test_comment_2():
    result = parse_metaprompt("[# asd ]]")
    assert result["exprs"] == [
        comment([{"text": " asd ", "type": "text"}]),
        t("]"),
    ]


def test_absence_of_comment():
    result = parse_metaprompt("# asd")
    assert result["exprs"] == [t("# asd")]


def test_meta():
    result = parse_metaprompt("[:test]")
    assert result["exprs"] == [var("test")]


def test_meta_text():
    result = parse_metaprompt("[:test]asd")
    assert result["exprs"] == [
        {"name": "test", "type": "var"},
        {"text": "asd", "type": "text"},
    ]


def test_meta_text2():
    result = parse_metaprompt("asd[:test]asd")
    assert result["exprs"] == [
        {"text": "asd", "type": "text"},
        {"name": "test", "type": "var"},
        {"text": "asd", "type": "text"},
    ]


def test_if():
    result = parse_metaprompt("[:if foo :then bar]")
    assert result["exprs"] == [
        if_then(
            [{"type": "text", "text": " foo "}],
            [{"type": "text", "text": " bar"}],
        )
    ]


def test_if_nested():
    result = parse_metaprompt("[:if [:if bar :then baz :else qux] :then bar]")
    assert result["exprs"] == [
        if_then(
            [
                # t(" "), <- removed by parse_utils.remove_extra_whitespace
                if_then_else([t(" bar ")], [t(" baz ")], [t(" qux")]),
                t(" "),
            ],
            [t(" bar")],
        )
    ]


def test_dummy_meta():
    result = parse_metaprompt("[test]")
    assert result["exprs"] == [t("[test]")]


def test_dummy_meta2():
    result = parse_metaprompt("[[]]")
    assert result["exprs"] == [t("[[]]")]


def test_dummy_meta3():
    result = parse_metaprompt("[a")
    assert result["exprs"] == [t("[a")]


def test_dummy_meta4():
    result = parse_metaprompt("[[][]]")
    assert result["exprs"] == [t("[[][]]")]


def test_meta2():
    result = parse_metaprompt("[$ []]")
    assert result["exprs"] == [meta([t(" []")])]


def test_meta3():
    result = parse_metaprompt("[var$ []]")
    assert result["exprs"] == [meta([t(" []")], chat_id="var")]


def test_meta4():
    result = parse_metaprompt("[VAR_FOO$ []]")
    assert result["exprs"] == [meta([t(" []")], chat_id="VAR_FOO")]


def test_meta_dollar():
    result = parse_metaprompt("[$ foo]")
    assert result["exprs"] == [meta([t(" foo")])]


def test_meta_dollar2():
    result = parse_metaprompt("[$ foo][$ foo]")
    assert result["exprs"] == [
        meta([t(" foo")]),
        meta([t(" foo")]),
    ]


def test_meta_dollar2():
    result = parse_metaprompt("[$ foo]]")
    assert result["exprs"] == [
        meta([t(" foo")]),
        t("]"),
    ]


def test_assign():
    result = parse_metaprompt("[:foo=bar]")
    assert result["exprs"] == [assign("foo", [{"type": "text", "text": "bar"}])]


def test_assign_optional():
    result = parse_metaprompt("[:foo?=bar]")
    assert result["exprs"] == [
        assign("foo", [{"type": "text", "text": "bar"}], required=False)
    ]


def test_assign_trailing_bracket():
    result = parse_metaprompt("[:foo=bar]]")
    assert result["exprs"] == [
        assign("foo", [{"type": "text", "text": "bar"}]),
        t("]"),
    ]


def test_assign_normal():
    result = parse_metaprompt("[:foo=[$ hi ]]")
    assert result["exprs"] == [
        {
            "type": "assign",
            "required": True,
            "name": "foo",
            "exprs": [meta([t(" hi ")])],
        }
    ]


def test_use_1():
    result = parse_metaprompt("[:use foo]")
    assert result["exprs"] == [use("foo", {})]


def test_use_2():
    result = parse_metaprompt("[:use foo :asd=hey :foo=bar]")
    assert result["exprs"] == [
        use(
            "foo",
            {
                "asd": [t("hey ")],
                "foo": [t("bar")],
            },
        )
    ]


def test_use_3():
    result = parse_metaprompt("[:use\nfoo\n]")
    assert result["exprs"] == [
        {"type": "use", "module_name": "foo", "parameters": {}}
    ]


def test_use_nested():
    result = parse_metaprompt("[:use foo :asd=[:use bar] hiii :foo=bar]")
    assert result["exprs"] == [
        {
            "type": "use",
            "module_name": "foo",
            "parameters": {
                "asd": [use("bar", {}), t(" hiii ")],
                "foo": [t("bar")],
            },
        }
    ]


def test_use_nested_2():
    result = parse_metaprompt(
        "[:use foo :asd=[hiiii [:use bar :qux=asd]] hiii :foo=bar]"
    )
    assert result["exprs"] == [
        {
            "type": "use",
            "module_name": "foo",
            "parameters": {
                "asd": [
                    t("[hiiii "),
                    use("bar", {"qux": [t("asd")]}),
                    t("] hiii "),
                ],
                "foo": [{"type": "text", "text": "bar"}],
            },
        }
    ]


def test_choose():
    result = parse_metaprompt(
        "[:choose foo :option o1 :is d1 :option o2 :is d2 :default bar]"
    )
    assert result["exprs"] == [
        choose(
            [t(" foo ")],
            [
                option([t(" o1 ")], [t(" d1 ")]),
                option([t(" o2 ")], [t(" d2 ")]),
            ],
            [t(" bar")],
        )
    ]


def test_choose_no_default():
    result = parse_metaprompt(
        "[:choose foo :option o1 :is d1 :option o2 :is d2]"
    )
    assert result["exprs"] == [
        choose(
            [t(" foo ")],
            [
                option([t(" o1 ")], [t(" d1 ")]),
                option([t(" o2 ")], [t(" d2")]),
            ],
            None,
        )
    ]


def test_call():
    result = parse_metaprompt(
        "[@writeFile :with filename.txt :with hello, world!]"
    )
    assert result["exprs"] == [
        call("writeFile", [[t(" filename.txt ")], [t(" hello, world!")]], {})
    ]


def test_extra_ws_1():
    assert remove_extra_whitespace(
        [
            assign("asd", []),
            t("\n"),
            assign("asd", []),
        ]
    ) == [
        assign("asd", []),
        assign("asd", []),
    ]


# TODO: more tests for remove_extra_whitespace
def test_extra_ws_2():
    assert remove_extra_whitespace(
        [
            t("\n"),
            assign("asd", []),
        ]
    ) == [
        assign("asd", []),
    ]
