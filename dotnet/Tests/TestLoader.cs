using System;
using System.Collections.Generic;
using System.Text.Json;
using Antlr4.Runtime;
using MetaPrompt.Utils;
using NUnit.Framework;

[TestFixture]
public class TestLoader
{
    [Test]
    public void TestExtractor1()
    {
        string prompt = "[:foo]";
        Assert.AreEqual(new HashSet<string> { "foo" }, VariableExtractor.ExtractVariables(prompt));
    }

    [Test]
    public void TestExtractor2()
    {
        string prompt = "[:foo][:bar]";
        Assert.AreEqual(new HashSet<string> { "foo", "bar" }, VariableExtractor.ExtractVariables(prompt));
    }

    [Test]
    public void TestExtractorAssign1()
    {
        string prompt = "[:foo=baz][:bar]";
        Assert.AreEqual(new HashSet<string> { "bar" }, VariableExtractor.ExtractVariables(prompt));
    }

    [Test]
    public void TestExtractorAssign2()
    {
        string prompt = "[:foo=baz][:foo]";
        Assert.AreEqual(new HashSet<string>(), VariableExtractor.ExtractVariables(prompt));
    }

    [Test]
    public void TestExtractorAssign3()
    {
        string prompt = "[:foo][:foo=baz] - first used, then assigned";
        Assert.AreEqual(new HashSet<string> { "foo" }, VariableExtractor.ExtractVariables(prompt));
    }
}