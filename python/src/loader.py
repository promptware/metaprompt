def _discover_variables(ast):
    if isinstance(ast, list):
        for node in ast:
            yield from _discover_variables(node)
    elif isinstance(ast, dict):
        if "type" in ast:
            if ast["type"] == "comment":
                return
            elif ast["type"] == "var":
                yield {"type": "var", "name": ast["name"]}
            elif ast["type"] == "assign":
                yield {"type": "assign", "name": ast["name"]}
        for key in ast:
            yield from _discover_variables(ast[key])


def extract_variables(ast):
    variables = set()
    assigned = set()
    for item in _discover_variables(ast):
        match item:
            case {"name": name, "type": "var"}:
                if name not in assigned:
                    variables.add(name)
            case {"name": name, "type": "assign"}:
                assigned.add(name)
    return variables
