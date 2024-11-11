# metaprompt

Metaprompt is a domain-specific language for LLM prompt engineering. It is a template engine for textual prompts, where expression expansion can depend on LLM outputs.

The goal is to extend the usual techniques of parametrized prompts with programmability, reusability and meta-prompting abilities.

## Quick example

```metaprompt
The text you are reading right now is a valid metaprompt program.

[# this is a comment that is ignored by the interpreter, that can be
used to add some info for the human-developer]

[# This whole text is a parametrized prompt, one of the parameters
being [:subject]]

[# [:subject] here is a variable reference. Variables can be defined
in-place, or passed from the external environment]

Give me a detailed poetic description of [:subject], using one or more
of the following metaphoric expressions:

[# Now I want to specialize my prompt depending on the value of
[:subject]. The output of the prompt below will be included *instead*
of the [$ ... block]: ]

[$ Write me a bullet list of metaphors for [:subject]. Do not produce
any other output]

[# Conditionals allow for logic branching: ]

[:if [:subject] is a human
 :then
   Use jokingly exaggerated style
 :else
   Include some references to [$ List some people who have any
   relation to [:subject], comma-separated]
]
```


See [`python/examples/`](./python/examples/) for more.

## Project status

This is an early work-in-progress. Follow [me on twitter](https://x.com/klntsky) for updates

- [ ] Finalize and specify the initial version of the syntax
- [ ] Implement a parser
  - [x] implement parse tree -> AST conversion
  - [ ] return error throwing to the parser
  - [ ] implement escaping
  - [x] `[:variable]` and `[:variable=some value]`
  - [ ] `[!assertion]`
  - [x] `[:if ... :then ... :else ...]`
  - [x] `[$ meta-prompt]`
  - [x] `[:include module :param1=value1]`
  - [ ] `[# comments]`
- [ ] Implement an evaluator
  - [x] meta-prompting
  - [x] conditionals
  - [x] externally-defined variables
  - [x] implement a 'manual' evaluator that asks the user to complete LLM inputs
  - [ ] API provider wrapper classes
    - [x] OpenAI
    - [ ] dynamic model switching
- [ ] Runtime system
  - [x] Support variable definition at runtime
  - [ ] exceptions
    - [ ] throwing exceptions
    - [ ] recovering from exceptions
- [ ] Utils
  - [ ] Unbound variable auto discovery to turn metaprompts into interfaces
- [ ] Add function definitions
  - [ ] enable function scopes
- [ ] Add a module system
- [ ] Add a package system
- [ ] Type system? TBD

## Notable sources of inspiration

- [llm-lang (Racket)](https://github.com/wilbowma/llm-lang) - similar in spirit. Does not support meta-prompting, uses racket as the DSL host language.
- [genaiscript (Microsoft)](https://github.com/microsoft/genaiscript) - a JS library, does not follow the "prompt-first" approach
- [LangChain prompt templates](https://python.langchain.com/docs/concepts/prompt_templates/) - only supports string substitution
- [Promptify](https://www.promptify.ai/explore) - focused on API creation.
- [Promptor](https://github.com/pikho/ppromptor) - prompt generator agent
