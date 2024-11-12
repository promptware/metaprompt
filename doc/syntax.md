# Text

A prompt is usually a valid metaprompt:

```metaprompt
Hi, LLM! How are you feeling today?
```

will be expanded to the same string, because it does not contain any MetaPrompt constructs.

# Variables

```metaprompt
Here's a variable: [:variable_name].

If a variable is used before first assignment, it is treated as a required
prompt parameter automatically.

[:variable_name=it can be reassigned to any value, however.
Including a value containing its old value: [:variable_name] or referencing [:other] variables]
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

[# ^ This expression will be expanded at runtime.

First, the following text will be fed to an LLM:

Please determine if the following statement is true.
Do not write any other output, answer just "true" or "false".
The statement: the sky is sometimes blue

The answer will determine the execution branch.
If the answer is not literally "true" or "false",
an exception will be thrown after a few retries
]
```

# Meta-prompting

```metaprompt
LLM says: [$ Hi, LLM! How are you today?]

[# ^^^ this prompt will be executed and its output will be inserted
at its position during expansion ]
```

A more inspiring example:

```metaprompt
[$ Improve this LLM prompt: [:prompt]]
```

# Modules

```metaprompt
[:use ./relative-import]
[:use package-name/directory/module]

With parameters:

[:use ./relative-import
 :someParameter= arbitrary value, potentially using
   any other MetaPrompt constructs
 :otherParameter= another value
]
```
