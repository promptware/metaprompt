# Overview

Metaprompt is a template language for LLM prompt automation, reuse and structuring, with support for writing prompts with prompts.

It adds a number of syntactic constructs to plaintext prompts, that get expanded at run time, producing textual output:

- variables
- conditionals
- LLM calls
- function calls
- etc.

# Project status

**!!! This is an early work-in-progress !!!**

Not all of the described features have been implemented.

[The repository README](https://github.com/promptware/metaprompt) will give you more details.

# Use cases

## Templating

MetaPrompt's basic use case is substituting parameter values instead of variable names embedded in a prompt:

```metaprompt
Write me a poem about [:subject] in the style of [:style]
```

## Prompt rewriting

Prompt rewriting is a technique of asking an LLM to create/modify/expand an LLM prompt.

- Dynamically crafting task-specific prompts based on a set of high level principles
- Modifying prompts to increase accuracy
- Securing inputs from prompt injection attacks and for content moderation
- Selecting the most suitable model based for a task

Quick example:

```metaprompt
[$ You are an LLM prompt engineer.
  Improve this prompt by adding specific details:
  [:prompt]
]
```

## Prompt structuring

A module system and a package system enable parameterized prompt reuse and publishing.

## Knowledge base maintenance

Organize your knowledge base in the form of multiple documents loaded conditionally on demand.

# Links

- [GitHub repo](https://github.com/promptware/metaprompt)
- [Documentation](https://docs.metaprompt-lang.org/)
- [Author's twitter](https://x.com/klntsky)
