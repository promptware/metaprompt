from invoke import task


@task
def build(c):
    parser_file = "src/MetaPrompt.g4"
    c.run(f"antlr4 -Dlanguage=Python3 -visitor {parser_file} -o ./python_gen")


@task
def check(c):
    c.run("black --check *.py")


@task
def format(c):
    c.run("black *.py")
