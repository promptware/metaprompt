# Text

A textual prompt is usually a valid metaprompt:

```metaprompt
Hi, LLM! How are you feeling today?
```

will be expanded to the same string, because it does not contain any MetaPrompt constructs.

# Variables

Variables should be referenced using this sintax: `[:variable_name]`. Variable names should match `[a-zA-Z_][a-zA-Z0-9_]*`.

The syntax for assignments is `[:variable_name=any expression]`.

Optional assignments use `?=` instead of `=` - they update the value only if a variable is unset.

# Comments

```metaprompt
[# Text for the human reader can be written like this.

   Comments must be well-formed metaprompt expressions too -
   in the future comment parse trees will be used to convey
   additional semantic info (e.g. documentation).

   Comments are ignored during evaluation.
]
```

# Conditionals

```metaprompt
[:if the sky is sometimes blue
 :then this...
 :else that...
]
```

`:if` expressions will be expanded at runtime.

First, the following text will be fed to an LLM:

```metaprompt
Please determine if the following statement is true.
Do not write any other output, answer just "true" or "false".
The statement: the sky is sometimes blue
```

The answer will determine the execution branch.
If the answer is not literally "true" or "false",
an exception will be thrown after a few retries

# Meta-prompting

```metaprompt
LLM says: [$ Hi, LLM! How are you today?]
```

The `[$` prompt will be executed and its output will be inserted
at its position during expansion. This enables powerful techniques
of prompt rewriting:

```metaprompt
[$ [$ Improve this LLM prompt: [:prompt]]]
```

Notice the double nesting of `[$` - the improved prompt will be fed back into an LLM.

## Chat history

Chat history can be preserved by assigning an ID to a prompt: `[some_chat_id$ ... ]`.

Subsequent invocations with the same chat ID *within the same module* will have a memory of the preceding conversation.

Chat IDs are actually variables that contain an entire chat history [(example usage)](../examples/roles.metaprompt).

# Escaping

`[` and `]` must be escaped using `\\`.

# Modules

Every `.metaprompt` file is a module. Conceptually, a module is a function that accepts a number of arguments, runs the executable parts, and returns text.

## File imports

The following expression will include `./relative-import.metaprompt` file (relative to the directory of the file, NOT to the current working dir):

```metaprompt
[:use ./relative-import]
```

## Package imports

**NOT IMPLEMENTED**

## Passing parameters

Unbound variables used in a module are its parameters, that must be provided when calling the module.

**Example**

Consider a file named [`hello.metaprompt`](../examples/hello.metaprompt):

```metaprompt
Hello, [:what]! [# `what` is a required parameter ]
[:who?=you]
[# ^ `who` is NOT a required parameter, because it is assigned
  before first use. However, optional assignment is used, so
  the default value can be overridden from the caller module
]
How are [:who] feeling today?
```

The `hello` module can be used from [another module](../examples/module-demo.metaprompt):

```
[:use ./hello :what=world :who=we]
```

## Special variables

### `MODEL` switching

`MODEL` variable is used to switch LLM models on the fly [(example)](../examples/model-change.metaprompt).

`MODEL` switching only works before an `[:if ...` or a `[$ ... ]` block:

```metaprompt
[:MODEL=gpt-4o]
[$ will be run in 4o,
  [:MODEL=gpt-3.5-turbo]
  [$ but this prompt will run in 3.5-turbo ]
]
```

Dynamic model selection based on a given task description allows to save costs by avoiding calls to costly models when possible [(example)](../examples/model-selection-demo.metaprompt).

### `ROLE` switching

`ROLE` is a special variable used to control LLM input "role".

`ROLE` can be assigned to one of three values:

- `system`: defines the behavior, scope, and context of the LLM.
- `user`: represents the individual interacting with the LLM.
- `assistant`: represents the LLM itself, responding to the user within the context defined by the system.

See [OpenAI docs](https://platform.openai.com/docs/guides/text-generation) for more info on roles.

[(example)](../examples/roles.metaprompt)

### Live `STATUS` update

`STATUS` variable provides a way to set a status line that is visible in the terminal. Useful to make the user aware of what is happening when no output is being generated:

```metaprompt
[:STATUS=running a marathon]
[$ ... long running task ]
[:STATUS=launching the rockets]
[$ ... another long running task ]
```

[(example)](../examples/model-selection-demo.metaprompt)
