def _is_silent_expr(ast):
    return ast["type"] == "assign" or ast["type"] == "comment"


def _is_ws_text(expr):
    return expr["type"] == "text" and expr["text"].strip() == ""


def scan(fst, f, lst):
    if len(lst) < 2:
        return lst
    i = 1
    length = len(lst)
    res = [lst[0]] if fst(lst[0]) else []
    while i < length:
        prev = lst[i - 1]
        curr = lst[i]
        if f(prev, curr):
            res.append(curr)
        i += 1
    return res


def remove_extra_whitespace(exprs):
    return scan(
        lambda first: not _is_ws_text(first),
        lambda prev, curr: not (_is_silent_expr(prev) and _is_ws_text(curr)),
        exprs,
    )


def join_text_pieces(children):
    """Joins multiple consequent text chunks into one:
    '[' 'foo' ']' -> '[foo]'
    (workaround for generated parser implementation details)
    """
    # TODO: move this to visit_exprs
    buf = None
    res = []
    for child in children:
        if buf is None:
            if child["type"] == "text":
                buf = child
            else:
                res.append(child)
        else:
            if child["type"] == "text":
                buf["text"] += child["text"]
            else:
                res.append(buf)
                buf = None
                res.append(child)
    if buf is not None:
        res.append(buf)

    return res
