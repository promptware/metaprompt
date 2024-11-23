class Argument:
    def __init__(self, compute, ast):
        self._compute = compute
        self._ast = ast
        self._value = None
        self._computed = False

    async def compute(self):
        if self._computed:
            return self._value
        res = await self._compute()
        self._value = res
        self._ast = None # allow gc to collect AST
        self._computed = True
        return res

    async def get_ast(self):
        return self._ast
