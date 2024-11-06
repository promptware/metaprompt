from invoke import task


@task
def build(c):
    parser_file = "src/MetaPrompt.g4"
    # lexer_file = "src/MetaPromptLexer.g4"

    # c.run(f"antlr4 -Dlanguage=Python3 -visitor {lexer_file} -o ./lexer")
    c.run(f"antlr4 -Dlanguage=Python3 -visitor {parser_file} -o ./python_gen")
    # c.run(f"antlr4 -Dlanguage=JavaScript -visitor {parser_file} -o ./js_gen")


@task
def check(c):
    c.run("black --check *.py")
