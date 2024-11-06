from invoke import task

@task
def build(c):
    parser_file = "src/MetaPrompt.g4"
    # c.run(f"antlr4 -Dlanguage=JavaScript -visitor {parser_file} -o ./js_gen")
