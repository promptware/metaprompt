from ffi import foreign_function, eager, lazy

# Logic


def booleanify(string):
    string = string.strip()
    if string in ["false", "true"]:
        return string == "true"
    else:
        raise ValueError(string + " is not a boolean")


@foreign_function(eager)
async def xor(*args, **kwargs):
    res = False
    for arg in args:
        res = not res if booleanify(arg) else res
    for _, arg in kwargs.items():
        res = not res if booleanify(arg) else res
    return "true" if res else "false"


@foreign_function(lazy)
async def _or(*args, **kwargs):
    for arg in args:
        arg = await arg.compute()
        if booleanify(arg):
            return "true"

    for _, arg in kwargs.items():
        arg = await arg.compute()
        if booleanify(arg):
            return "true"

    return "false"


@foreign_function(lazy)
async def _and(*args, **kwargs):
    for arg in args:
        arg = await arg.compute()
        if not booleanify(arg):
            return "false"

    for _, arg in kwargs.items():
        arg = await arg.compute()
        if not booleanify(arg):
            return "false"

    return "true"


# Strings


@foreign_function(eager)
async def cite(string, prefix="> "):
    return "\n".join([prefix + line for line in string.split("\n")])


@foreign_function(eager)
async def strip(string):
    return string.strip()

# TODO: strip lines
# TODO: replace
# TODO: strip suffix/prefix
# TODO: find

prelude = {
    "and": _and,
    "or": _or,
    "xor": xor,
    "cite": cite,
    "strip": strip,
}
