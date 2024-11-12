from invoke import task
import os


@task
def build(c):
    grammar = "../grammar/MetaPrompt.g4"
    c.run(f"cp -r {grammar} MetaPrompt.g4")
    c.run(f"antlr4 -Dlanguage=Python3 -visitor MetaPrompt.g4 -o ./src/parser")
    c.run(
        f"antlr4 -Dlanguage=JavaScript -visitor MetaPrompt.g4 -o ./js/metaprompt/parser"
    )
    c.run(f"rm MetaPrompt.g4")


@task
def check(c):
    c.run("black --check *.py src/*.py")


@task
def format(c):
    c.run("black *.py")
    c.run("black src/*.py")


@task
def clean(c):
    """Remove all __pycache__ directories recursively."""
    for root, dirs, files in os.walk("./src/"):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                pycache_path = os.path.join(root, dir_name)
                c.run(f"rm -rf {pycache_path}")
                print(f"Removed {pycache_path}")
