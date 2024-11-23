from parse_metaprompt import (
    parse_metaprompt,
    extract_tokens,
)
from parse_utils import remove_extra_whitespace


def parse(text):
    return parse_metaprompt(text)["exprs"]


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
    result = parse("")
    assert result == []


def test_text_0():
    result = parse("asd")
    assert result == [{"text": "asd", "type": "text"}]


def test_text_1():
    result = parse("$$")
    assert result == [t("$$")]


def test_text_2():
    result = parse("$=")
    assert result == [t("$=")]


def test_text_kw_is():
    result = parse(":is")
    assert result == [t(":is")]


def test_escaping():
    result = parse("\\")
    assert result == [t("\\")]


def test_escaping_1():
    result = parse("\\[")
    assert result == [t("[")]


def test_escaping_2():
    result = parse("\\[:foo\\]")
    assert result == [t("[:foo]")]


def test_escaping_2_1():
    result = parse("\\\\[:foo]")
    assert result == [t("\\\\"), var("foo")]


def test_escaping_2_2():
    result = parse("\\\\")
    assert result == [t("\\\\")]


def test_escaping_3():
    result = parse("\\[:foo")
    assert result == [t("[:foo")]


def test_escaping_4():
    bs="\\"
    result = parse(f"{bs}{bs}{bs}[")
    assert result == [t(f"{bs}[")]


def test_escaping_5():
    result = parse("\\  \\")
    assert result == [t("\\  \\")]


def test_comment():
    result = parse("[# asd ]")
    assert result == [comment([{"text": " asd ", "type": "text"}])]


def test_comment_2():
    result = parse("[# asd ]]")
    assert result == [
        comment([{"text": " asd ", "type": "text"}]),
        t("]"),
    ]


def test_absence_of_comment():
    result = parse("# asd")
    assert result == [t("# asd")]


def test_meta():
    result = parse("[:test]")
    assert result == [var("test")]


def test_meta_text():
    result = parse("[:test]asd")
    assert result == [
        {"name": "test", "type": "var"},
        {"text": "asd", "type": "text"},
    ]


def test_meta_text2():
    result = parse("asd[:test]asd")
    assert result == [
        {"text": "asd", "type": "text"},
        {"name": "test", "type": "var"},
        {"text": "asd", "type": "text"},
    ]


def test_if():
    result = parse("[:if foo :then bar]")
    assert result == [
        if_then(
            [{"type": "text", "text": " foo "}],
            [{"type": "text", "text": " bar"}],
        )
    ]


def test_if_nested():
    result = parse("[:if [:if bar :then baz :else qux] :then bar]")
    assert result == [
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
    result = parse("\[test\]")
    assert result == [t("[test]")]


def test_dummy_meta2():
    result = parse("\\[\\[\\]\\]")
    assert result == [t("[[]]")]


def test_dummy_meta3():
    result = parse("\\[a")
    assert result == [t("\\[a")]


def test_dummy_meta4():
    result = parse("\\[\\[\\]\\[\\]\\]")
    assert result == [t("[[][]]")]


def test_meta2():
    result = parse("[$ \\[\\]]")
    assert result == [meta([t(" []")])]


def test_meta3():
    result = parse("[var$ []]")
    assert result == [meta([t(" []")], chat_id="var")]


def test_meta4():
    result = parse("[VAR_FOO$ []]")
    assert result == [meta([t(" []")], chat_id="VAR_FOO")]


def test_meta_dollar():
    result = parse("[$ foo]")
    assert result == [meta([t(" foo")])]


def test_meta_dollar2():
    result = parse("[$ foo][$ foo]")
    assert result == [
        meta([t(" foo")]),
        meta([t(" foo")]),
    ]


def test_meta_dollar2():
    result = parse("[$ foo]]")
    assert result == [
        meta([t(" foo")]),
        t("]"),
    ]


def test_assign():
    result = parse("[:foo=bar]")
    assert result == [assign("foo", [{"type": "text", "text": "bar"}])]


def test_assign_optional():
    result = parse("[:foo?=bar]")
    assert result == [
        assign("foo", [{"type": "text", "text": "bar"}], required=False)
    ]


def test_assign_trailing_bracket():
    result = parse("[:foo=bar]]")
    assert result == [
        assign("foo", [{"type": "text", "text": "bar"}]),
        t("]"),
    ]


def test_assign_normal():
    result = parse("[:foo=[$ hi ]]")
    assert result == [
        {
            "type": "assign",
            "required": True,
            "name": "foo",
            "exprs": [meta([t(" hi ")])],
        }
    ]


def test_use_1():
    result = parse("[:use foo]")
    assert result == [use("foo", {})]


def test_use_2():
    result = parse("[:use foo :asd=hey :foo=bar]")
    assert result == [
        use(
            "foo",
            {
                "asd": [t("hey ")],
                "foo": [t("bar")],
            },
        )
    ]


def test_use_3():
    result = parse("[:use\nfoo\n]")
    assert result == [{"type": "use", "module_name": "foo", "parameters": {}}]


def test_use_nested():
    result = parse("[:use foo :asd=[:use bar] hiii :foo=bar]")
    assert result == [
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
    result = parse("[:use foo :asd=\\[hiiii [:use bar :qux=asd]\\] hiii :foo=bar]")
    assert result == [
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
    result = parse(
        "[:choose foo :option o1 :is d1 :option o2 :is d2 :default bar]"
    )
    assert result == [
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
    result = parse("[:choose foo :option o1 :is d1 :option o2 :is d2]")
    assert result == [
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
    result = parse("[@writeFile filename.txt :with hello, world!]")
    assert result == [
        call("writeFile", [[t("filename.txt ")], [t(" hello, world!")]], {})
    ]


def test_call_1():
    result = parse("[@writeFile]")
    assert result == [call("writeFile", [], {})]


def test_call_2():
    result = parse("[@writeFile:file=file.txt]")
    assert result == [call("writeFile", [], {"file": [t("file.txt")]})]


def test_call_3():
    result = parse("[@cite hello]")
    assert result == [call("cite", [[t("hello")]], {})]


def test_call_4():
    result = parse("[@cite hello :with hi]")
    assert result == [call("cite", [[t("hello ")], [t(" hi")]], {})]


def test_call_5():
    result = parse("[@cite :param=1 :with hi]")
    assert result == [call("cite", [[t(" hi")]], {"param": [t("1 ")]})]


def test_call_6():
    result = parse("[@cite :with hi]")
    assert result == [call("cite", [[t(" hi")]], {})]


def test_call_named():
    result = parse("[@writeFile :file=filename.txt :content=hello, world!]")
    assert result == [
        call(
            "writeFile",
            [],
            {
                "file": [t("filename.txt ")],
                "content": [t("hello, world!")],
            },
        )
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
