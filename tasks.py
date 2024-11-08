from invoke import task


@task
def build(c):
    grammar = "./grammar/MetaPrompt.g4"
    c.run(f"antlr4 -Dlanguage=Python3 -visitor {grammar} -o ./python/metaprompt/parser")
    c.run(f"antlr4 -Dlanguage=JavaScript -visitor {grammar} -o ./js/metaprompt/parser")


@task
def check(c):
    c.run("black --check *.py")


@task
def format(c):
    c.run("black *.py")
    c.run("black python/metaprompt/*.py")
