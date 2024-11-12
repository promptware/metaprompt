# Overview

Metaprompt is a language for prompt automation, structuring and reuse.

One one side, it is very similar to a template engine like Jinja or EJS. The twist is, metaprompt expansion depends on LLM outputs of LLM queries, that are formed in natural language.

# Use cases

## Prompt organization

A module system and a package system allow anyone to assign identities to promps and package them as callable functions.

## Meta-prompting

Meta-prompting is a technique of asking an LLM to create an LLM prompt.

- Using prompts to craft task-specific prompts based on a set of high level principles
- Modifying prompts to increase accuracy
- Securing inputs from prompt injection attacks
- Model selection based on prompt contents

## Templating

The most basic use case of metaprompt is substituting parameter values instead of variable names embedded in a prompt.
