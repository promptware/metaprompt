from typing import Set


class ParameterSet:
    def __init__(
        self,
        required: Set[str] = None,
        optional: Set[str] = None,
        assigned: Set[str] = None,
    ):
        if required is None:
            required = set()
        if optional is None:
            optional = set()
        if assigned is None:
            assigned = set()
        self.required = required
        self.optional = optional
        self.assigned = assigned

    def __eq__(self, other):
        return (
            self.required == other.required
            and self.optional == other.optional
            and self.assigned == other.assigned
        )

    def then(self, other):
        """Implements sequential composition of ParameterSets:
        params([expr1, expr2]) = params(expr1).then(params(expr2))
        """
        return ParameterSet(
            # required
            self.required.union(other.required.difference(self.assigned)),
            # optional
            self.optional.union(other.optional)
            .difference(self.required)
            .difference(other.required),
            # assigned
            self.assigned.union(other.assigned),
        )

    def alternative(self, other):
        """Implements parallel composition of ParameterSets, that is used
        for :if: either of the alternatives can be executed, so we have to be
        conservative.
        """
        return ParameterSet(
            # required: all of the required variables are required,
            # we don't know which branch will be chosen
            self.required.union(other.required),
            # optional: if something is optional in just one of the branches,
            # it is optional in the whole expression, but if it required in
            # either, it is required in the whole
            self.optional.union(other.optional)
            .difference(self.required)
            .difference(other.required),
            # assigned: something must be assigned in both branches for us to
            # be sure it is assigned
            self.assigned.intersection(other.assigned),
        )

    def assign_var(self, name):
        """handles [:name=value]"""
        self.assigned.add(name)

    def assign_var_optional(self, name):
        """handles [:name?=value]"""
        if name not in self.assigned:
            self.optional.add(name)
            self.assigned.add(name)

    def use_var(self, name):
        if name not in self.assigned:
            self.required.add(name)


def extract_parameter_set(ast):
    # TODO: special handling of ROLE, MODEL variables
    res = ParameterSet()

    if isinstance(ast, list):
        for node in ast:
            res = res.then(extract_parameter_set(node))
    elif isinstance(ast, dict) and "type" in ast:
        if ast["type"] == "text":
            pass
        elif ast["type"] == "metaprompt":
            for expr in ast["exprs"]:
                res = res.then(extract_parameter_set(expr))
        elif ast["type"] == "var":
            res.use_var(ast["name"])
        elif ast["type"] == "use":
            for _, expr in ast["exprs"]:
                res = res.then(extract_parameter_set(expr))
        elif ast["type"] == "assign":
            if ast["required"]:
                res.assign_var(ast["name"])
            else:
                res.assign_var_optional(ast["name"])
        elif ast["type"] == "meta":
            for expr in ast["exprs"]:
                res = res.then(extract_parameter_set(expr))
        elif ast["type"] == "exprs":
            for expr in ast["exprs"]:
                extract_parameter_set(expr, assigned)
        elif ast["type"] == "comment":
            pass
        elif ast["type"] == "if_then_else":
            res = res.then(extract_parameter_set(ast["condition"])).then(
                extract_parameter_set(ast["then"]).alternative(
                    extract_parameter_set(ast["else"])
                )
            )
        else:
            raise ValueError(
                "extract_parameter_set: unknown AST expression: " + str(ast)
            )
    else:
        raise ValueError(
            "extract_parameter_set: unknown AST expression: " + str(ast)
        )

    return res
