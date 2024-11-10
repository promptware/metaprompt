using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using Antlr4.Runtime;
using Antlr4.Runtime.Tree;
using MetaPrompt;
using MetaPrompt.AntlrErrorListeners;

public static class ParseMetaprompt
{
    public static Dictionary<string, object> Parse(string prompt)
    {
        var inputStream = new AntlrInputStream(prompt);
        var lexer = new MetaPromptLexer(inputStream);
        var tokenStream = new CommonTokenStream(lexer);
        var parser = new MetaPromptParser(tokenStream);

        parser.RemoveErrorListeners();
        parser.AddErrorListener(new ThrowingErrorListener());

        var tree = parser.prompt();
        var visitor = new MetaPromptASTBuilder();
        var exprs = visitor.Visit(tree);

        if (exprs != null && exprs.Count > 0)
        {
            return exprs[0];
        }
        else
        {
            throw new Exception("Failed to parse metaprompt");
        }
    }
}