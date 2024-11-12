from parse_metaprompt import parse_metaprompt, extract_tokens


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


def meta(exprs):
    return {
        'type': 'meta',
        'exprs': exprs
    }

def use(module_name, parameters):
    return {
        'type': 'use',
        'module_name': module_name,
        'parameters': parameters
    }

def test_empty():
    result = parse_metaprompt("")
    assert result["exprs"] == []


def test_text():
    result = parse_metaprompt("asd")
    assert result["exprs"] == [{"text": "asd", "type": "text"}]


def test_comment():
    result = parse_metaprompt("[# asd ]")
    assert result["exprs"] == [comment([{"text": " asd ", "type": "text"}])]


def test_absence_of_comment():
    result = parse_metaprompt("# asd")
    assert result["exprs"] == [t("#"), t(" asd")]


def test_meta():
    result = parse_metaprompt("[:test]")
    assert result["exprs"] == [{"name": "test", "type": "var"}]


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
                t(" "),
                if_then_else([t(" bar ")], [t(" baz ")], [t(" qux")]),
                t(" "),
            ],
            [t(" bar")],
        )
    ]


def test_dummy_meta():
    result = parse_metaprompt("[test]")
    assert result["exprs"] == [t("["), t("test"), t("]")]


def test_dummy_meta2():
    result = parse_metaprompt("[[]]")
    assert result["exprs"] == [t("["), t("["), t("]"), t("]")]



def test_dummy_meta3():
    result = parse_metaprompt("[a")
    assert result["exprs"] == [t("["), t("a")]


def test_dummy_meta2():
    result = parse_metaprompt("[[][]]")
    assert result["exprs"] == [t("["), t("["), t("]"), t("["), t("]"), t("]")]


def test_meta_dollar():
    result = parse_metaprompt("[$ foo]")
    assert result["exprs"] == [{'type': 'meta', 'exprs': [ {'type': 'text', 'text': " foo"}]}]


def test_meta_dollar2():
    result = parse_metaprompt("[$ foo][$ foo]")
    assert result["exprs"] == [
        {'type': 'meta', 'exprs': [ {'type': 'text', 'text': " foo"}]},
        {'type': 'meta', 'exprs': [ {'type': 'text', 'text': " foo"}]},
    ]


def test_meta_dollar2():
    result = parse_metaprompt("[$ foo]]")
    assert result["exprs"] == [
        {'type': 'meta', 'exprs': [ {'type': 'text', 'text': " foo"}]},
        t("]")
    ]


def test_assign():
    result = parse_metaprompt("[:foo=bar]")
    assert result["exprs"] == [{'type': 'assign', 'name': 'foo', 'exprs': [ {'type': 'text', 'text': "bar"}]}]


def test_assign_trailing_bracket():
    result = parse_metaprompt("[:foo=bar]]")
    assert result["exprs"] == [
        {'type': 'assign', 'name': 'foo',
         'exprs': [ {'type': 'text', 'text': "bar"}]
         },
        t(']')
    ]


def test_assign_trailing_bracket():
    result = parse_metaprompt("[:foo=[$ hi ]]")
    assert result["exprs"] == [
        {
            'type': 'assign', 'name': 'foo',
            'exprs': [
                meta(
                    [ t(" hi ") ]
                )
            ]
        }
    ]

def test_use_1():
    result = parse_metaprompt("[:use foo]")
    assert result["exprs"] == [
        {
            'type': 'use',
            'module_name': 'foo',
            'parameters': {}
        }
    ]


def test_use_2():
    result = parse_metaprompt("[:use foo :asd=hey :foo=bar]")
    assert result["exprs"] == [
        {
            'type': 'use',
            'module_name': 'foo',
            'parameters': {
                'asd': [ { 'type': 'text', 'text': 'hey ' } ],
                'foo': [ { 'type': 'text', 'text': 'bar' } ]
            }
        }
    ]


def test_use_3():
    result = parse_metaprompt("[:use\nfoo\n]")
    assert result["exprs"] == [
        {
            'type': 'use',
            'module_name': 'foo',
            'parameters': {}
        }
    ]


def test_use_nested():
    result = parse_metaprompt(
        "[:use foo :asd=[:use bar] hiii :foo=bar]"
    )
    assert result["exprs"] == [
        {
            'type': 'use',
            'module_name': 'foo',
            'parameters': {
                'asd': [
                    use('bar', {}),
                    { 'type': 'text', 'text': ' hiii ' }
                ],
                'foo': [ { 'type': 'text', 'text': 'bar' } ]
            }
        }
    ]


def test_use_nested_2():
    result = parse_metaprompt(
        "[:use foo :asd=[hiiii [:use bar :qux=asd]] hiii :foo=bar]"
    )
    assert result["exprs"] == [
        {
            'type': 'use',
            'module_name': 'foo',
            'parameters': {
                'asd': [
                    t('['),
                    t('hiiii '),
                    use('bar', {'qux': [t('asd')]}),
                    t(']'),
                    { 'type': 'text', 'text': ' hiii ' },
                ],
                'foo': [ { 'type': 'text', 'text': 'bar' } ]
            }
        }
    ]
