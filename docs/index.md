# Overview

Metaprompt is a template language for LLM prompt automation, reuse and structuring, with support for writing prompts with prompts.

It adds a number of syntactic constructs to plaintext prompts:

- variables
- conditionals
- function calls
- meta-prompting operator
- etc.

These constructs get expanded at run time, producing textual output.

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

## Meta-prompting

Meta-prompting is a technique of asking an LLM to create/modify/expand an LLM prompt.

- Dynamically crafting task-specific prompts based on a set of high level principles
- Modifying prompts to increase accuracy
- Securing inputs from prompt injection attacks
- Selecting the most suitable model based on prompt contents

Quick example:

```metaprompt
[$ You are an LLM prompt engineer.
  Improve this prompt by adding specific instructions:
  [:prompt]
]
```

## Prompt structuring

A module system and a package system enable parameterized prompt reuse and publishing.

```metaprompt
# hello.metaprompt:
Hello, [:what]!
```

```metaprompt
# main.metaprompt:
[:use ./hello :what=world]
```

`main.metaprompt` will evaluate to `Hello, world!`
