# Text

A textual prompt is usually a valid metaprompt:

```metaprompt
Hi, LLM! How are you feeling today?
```

will be expanded to the same string, because it does not contain any MetaPrompt constructs.

# Variables

```metaprompt
Here's a variable: [:variable_name].

If a variable is used before first assignment, it is treated as a required
prompt parameter automatically.

[:variable_name=it can be reassigned to any value, however]
[:variable_name=Including a value containing its old value: [:variable_name]]
```

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

# Escaping

Normally, you would not need escaping, e.g. `[:foo` will evaluate to `[:foo` as text. But if you want to specify a MetaPrompt expression literally, use `\` before the `[` character: `\[:foo]` will evaluate to `[:foo]` as text, without special meaning. You can escape `\` with another `\`, but only if it is positioned before a `[`:

`\foo` → (text `\foo`)

`\\` → (text `\\`)

`\[:foo]` → (text `[:foo]`)

`\\[:foo]` → (text `\\`) (variable `foo`)

`\[some text` -> (text `[some text`) - note that in this case the `\` character disappears, although escaping does not happen because `[some text` is not a special MetaPrompt construct.

# Modules

Every `.metaprompt` file is a function.

Unbound variables used in a file are its parameters, that must be provided.

```metaprompt
Hello, [:what]! [# `what` is a parameter ]
[:who=you] [# `who` is NOT a parameter, because it is assigned before first use]
How are [:who] feeling today?
```

## File imports

The following expression will include `./relative-import.metaprompt` file (relative to the directory of the file, NOT to the current working dir):

```metaprompt
[:use ./relative-import]
```

## Package imports

**NOT IMPLEMENTED**

## Passing parameters

```
[:use ./relative-import
 :someParameter= arbitrary value, potentially using
   any other MetaPrompt constructs
 :otherParameter= another value
]
```

## Special variables

- `MODEL` - used to determine active LLM id.
