from invoke import task

@task
def build(c):
    grammar_file = "src/MetaPrompt.g4"
    c.run(f"antlr4 -Dlanguage=Python3 -visitor {grammar_file} -o ./python_gen")
    c.run(f"antlr4 -Dlanguage=JavaScript -visitor {grammar_file} -o ./js_gen")
