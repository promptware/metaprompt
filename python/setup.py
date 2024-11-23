from setuptools import setup, find_packages
import pathlib

# Read the README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="metaprompt",
    version="0.0.1",
    description="A template engine for LLM prompts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vladimir Kalnitsky",
    author_email="klntsky@gmail.com",
    url="https://metaprompt-lang.org",
    license="Unlicense",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "antlr4-python3-runtime>=4.13.2",
        "openai>=1.54.3",
        "python-dotenv>=1.0.1",
        "setuptools>=68.1.2",
        "requests>=2.32.2",
        "html2text",
    ],
    extras_require={
        "dev": [
            "invoke>=2.2.0",
            "pytest>=8.3.3",
            "pytest-asyncio>=0.24.0",
            "flake8>=3.8.4",
            "black>=24.10.0",
            "antlr4-tools==0.2.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "metaprompt=main:main",
        ],
    },
)
