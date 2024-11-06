from setuptools import setup, find_packages

setup(
    name="metaprompt-parser",
    version="0.0.1",
    description="https://metaprompt-lang.org/",
    author="Vladimir Kalnitsky",
    author_email="klntsky@gmail.com",
    url="https://github.com/promptware/metaprompt",
    packages=find_packages(),
    extras_require={
        "dev": [
            "black",
            "flake8",
            "pytest",
            "mypy",
            "pip-tools",
            "invoke",
        ],
    },
    install_requires=[
        "antlr4-python3-runtime==4.13.2",
        "antlr4-tools==0.2.1",
        "install-jdk==1.1.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
