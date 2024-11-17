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


See [`examples/`](./examples/) for more.

## Project status

This is an early work-in-progress. Follow [me on twitter](https://x.com/klntsky) for updates

- [ ] Specify the initial version of the syntax
- [ ] Implement a parser
  - [x] implement parse tree -> AST conversion
  - [x] return error throwing to the parser
  - [x] implement escaping
  - [x] `[:variable]` and `[:variable=some value]`
  - [x] `[:if ... :then ... :else ...]`
  - [x] `[$ meta-prompt]`
  - [x] `[:use module :param1=value1]`
  - [x] `[# comments]`
  - [ ] `[:status some-status]` - to show during prompt evaluation
  - [ ] `[:call ffi-function :param1=foo :param2=bar]`
  - [ ] syntax for ignoring `$` output
- [ ] Implement an evaluator
  - [x] meta-prompting
  - [x] conditionals
  - [x] externally-defined variables
  - [x] implement a 'manual' evaluator that asks the user to complete LLM inputs
  - [ ] API provider wrapper classes
    - [x] OpenAI
    - [ ] Anthropic
    - [ ] llama
- [ ] Runtime system
  - [x] Support variable definition at runtime
  - [x] dynamic model switching (via `MODEL` variable - [example](./examples/model-change.metaprompt))
  - [x] Multiple chat instances and ability to switch between them, to distribute data between chat contexts. E.g. `[chat1$ the object is the moon][chat1$ what is the object?]` [(example)](./examples/chat-history.metaprompt)
  - [ ] message role system (system, user)
  - [ ] exceptions
    - [ ] throwing exceptions
    - [ ] recovering from exceptions
  - [ ] LLM output validation?
    - [ ] via regexps?
    - [ ] via parsing?
- [ ] FFI
  - [ ] syntax - preferably via `[:use @ffi-function :param1=foo :param2=bar]`
  - [ ] how to throw exceptions from FFI
  - [ ] API
  - [ ] standard library
    - [ ] text processing
    - [ ] shell access
    - [ ] running executables
    - [ ] file system access
      - [ ] isolation?
    - [ ] HTTP stack
- Utils
  - [x] Unbound variable auto discovery
  - [ ] Machinery to turn metaprompts into interfaces (parameters become form fields)
    - [ ] static validation?
- [ ] Add a module system
  - [x] syntax
  - [x] module loading at runtime
  - [ ] preload modules on startup - is needed?
  - [ ] module caching
  - [ ] tests
- [ ] Add a package system
  - [ ] specify package format
  - [ ] create a package registry
  - [ ] on-the-fly package installer

## Architecture decisions

- functions, files, and modules are essentially the same - invoked with `[:use ...]`
- metaprompt parameters are just variables that are not bound before first use - this and the above decision allow to get rid of function syntax entirely

### To consider

- dynamic module loading vs. static module loading: dynamic is lazy, so skips unneeded modules, but static loading guarantees absence of runtime errors due to module resolution failures (which saves costs)
- exception system. how to pass payloads with exceptions
- turning exceptions into continuations in spirit of [hurl](https://hurl.wtf)

## Notable sources of inspiration

- [llm-lang (Racket)](https://github.com/wilbowma/llm-lang) - similar in spirit. Does not support meta-prompting, uses racket as the DSL host language.
- [genaiscript (Microsoft)](https://github.com/microsoft/genaiscript) - a JS library, does not follow the "prompt-first" approach
- [PLang](https://plang.is/) - a language for task automation. Uses LLMs for control flow.
- [LangChain prompt templates](https://python.langchain.com/docs/concepts/prompt_templates/) - only supports string substitution
- [Promptify](https://www.promptify.ai/explore) - focused on API creation.
- [Promptor](https://github.com/pikho/ppromptor) - prompt generator agent
