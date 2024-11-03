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

## Project status

This is an early work-in-progress. Follow [me on twitter](https://x.com/klntsky) for updates

- [ ] Finalize the initial version of the syntax
- [ ] Implement a parser
- [ ] Implement an evaluator that supports meta-prompting, conditionals and externally-defined variables
- [ ] Support variable definition at runtime via a runtime system
- [ ] Add function definitions
- [ ] Type system? TBD
- [ ] Add a module system
