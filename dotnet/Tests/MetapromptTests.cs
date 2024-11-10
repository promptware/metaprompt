using System;
using System.Collections.Generic;
using Antlr4.Runtime;
using NUnit.Framework;

[TestFixture]
public class MetapromptTests
{
    private Dictionary<string, object> Text(string text) => new Dictionary<string, object>
    {
        { "type", "text" },
        { "text", text }
    };

    private Dictionary<string, object> Variable(string name) => new Dictionary<string, object>
    {
        { "type", "var" },
        { "name", name }
    };

    private Dictionary<string, object> IfThenElse(List<Dictionary<string, object>> condition, List<Dictionary<string, object>> thenBranch, List<Dictionary<string, object>> elseBranch) =>
        new Dictionary<string, object>
        {
            { "type", "if_then_else" },
            { "condition", condition },
            { "then", thenBranch },
            { "else", elseBranch }
        };

    private Dictionary<string, object> Meta(List<Dictionary<string, object>> exprs) =>
        new Dictionary<string, object>
        {
            { "type", "meta" },
            { "exprs", exprs }
        };

    private Dictionary<string, object> Assign(string name, List<Dictionary<string, object>> exprs) =>
        new Dictionary<string, object>
        {
            { "type", "assign" },
            { "name", name },
            { "exprs", exprs }
        };

    [Test]
    public void TestEmpty()
    {
        var result = ParseMetaprompt.Parse("");
        Assert.AreEqual(new List<Dictionary<string, object>>(), result["exprs"]);
    }

    [Test]
    public void TestText()
    {
        var result = ParseMetaprompt.Parse("asd");
        Assert.That(result["exprs"], Is.EqualTo(new List<Dictionary<string, object>> { Text("asd") }));
    }

    [Test]
    public void TestMeta()
    {
        var result = ParseMetaprompt.Parse("[:test]");
        Assert.AreEqual(new List<Dictionary<string, object>> { Variable("test") }, result["exprs"]);
    }

    [Test]
    public void TestMetaText()
    {
        var result = ParseMetaprompt.Parse("[:test]asd");
        Assert.AreEqual(new List<Dictionary<string, object>>
        {
            Variable("test"),
            Text("asd")
        }, result["exprs"]);
    }

    [Test]
    public void TestIf()
    {
        var result = ParseMetaprompt.Parse("[:if foo :then bar]");
        var expected = new List<Dictionary<string, object>> {
            IfThenElse(
                new List<Dictionary<string, object>> { Text(" foo ") },
                new List<Dictionary<string, object>> { Text(" bar") },
                new List<Dictionary<string, object>>()
            )
        };
        Assert.That(result["exprs"], Is.EqualTo(expected));
    }

    [Test]
    public void TestIfNested()
    {
        var result = ParseMetaprompt.Parse("[:if [:if bar :then baz :else qux] :then bar]");
        var expected = new List<Dictionary<string, object>> {
            IfThenElse(
                new List<Dictionary<string, object>> {
                    Text(" "),
                    IfThenElse(
                        new List<Dictionary<string, object>> { Text(" bar ") },
                        new List<Dictionary<string, object>> { Text(" baz ") },
                        new List<Dictionary<string, object>> { Text(" qux") }
                    ),
                    Text(" ")
                },
                new List<Dictionary<string, object>> { Text(" bar") },
                new List<Dictionary<string, object>>() // Empty else block for outer if
            )
        };
        Assert.That(result["exprs"], Is.EqualTo(expected));
    }

    [Test]
    public void TestDummyMeta()
    {
        var result = ParseMetaprompt.Parse("[test]");
        Assert.AreEqual(new List<Dictionary<string, object>>
        {
            Text("["),
            Text("test"),
            Text("]")
        }, result["exprs"]);
    }

    [Test]
    public void TestDummyMeta2()
    {
        var result = ParseMetaprompt.Parse("[[]]");
        Assert.AreEqual(new List<Dictionary<string, object>>
        {
            Text("["),
            Text("["),
            Text("]"),
            Text("]")
        }, result["exprs"]);
    }

    [Test]
    public void TestAssign()
    {
        var result = ParseMetaprompt.Parse("[:foo=bar]");
        Assert.AreEqual(new List<Dictionary<string, object>>
        {
            Assign("foo", new List<Dictionary<string, object>> { Text("bar") })
        }, result["exprs"]);
    }

    [Test]
    public void TestUnmatchedBrackets()
    {
        Assert.Throws<Exception>(() => ParseMetaprompt.Parse("[:if foo :then bar"));
        Assert.Throws<Exception>(() => ParseMetaprompt.Parse(":if foo :then bar]"));
        Assert.Throws<Exception>(() => ParseMetaprompt.Parse("[:if foo :then bar]]"));
    }

    [Test]
    public void TestAssignWithSpaces()
    {
        var result = ParseMetaprompt.Parse("[:foo=bar]");
        var expected = new List<Dictionary<string, object>> {
            Assign("foo", new List<Dictionary<string, object>> { Text("bar") })
        };
        Assert.AreEqual(expected, result["exprs"]);
    }

    [Test]
    public void TestVariableInText()
    {
        var result = ParseMetaprompt.Parse("Hello, [:name]! How are you?");
        var expected = new List<Dictionary<string, object>>
        {
            Text("Hello, "),
            Variable("name"),
            Text("! How are you?")
        };
        Assert.That(result["exprs"], Is.EqualTo(expected));
    }
}
