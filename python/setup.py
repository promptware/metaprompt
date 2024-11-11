from setuptools import setup, find_packages

setup(
    name="metaprompt",
    version="0.0.1",
    description="A template engine for LLM prompts",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
)
