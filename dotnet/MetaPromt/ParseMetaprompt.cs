using System;
using System.Collections.Generic;
using System.Linq;
using Antlr4.Runtime;
using Antlr4.Runtime.Tree;

public class ThrowingErrorListener : IAntlrErrorListener<IToken>
{
    public void SyntaxError(TextWriter output, IRecognizer recognizer, IToken offendingSymbol, int line, int charPositionInLine, string msg, RecognitionException e)
    {
        throw new Exception($"Syntax error at line {line}:{charPositionInLine} - {msg}");
    }
}

public class MetaPromptASTBuilder : MetaPromptBaseVisitor<Dictionary<string, object>>
{
    public override Dictionary<string, object> VisitPrompt(MetaPromptParser.PromptContext context)
    {
        var exprsNode = VisitExprs(context.exprs());
        return new Dictionary<string, object> { { "type", "metaprompt" }, { "exprs", exprsNode } };
    }

    public override Dictionary<string, object> VisitExprs(MetaPromptParser.ExprsContext context)
    {
        var exprs = new List<object>();
        foreach (var expr in context.expr())
        {
            var exprItems = VisitExpr(expr);
            exprs.AddRange((IEnumerable<object>)exprItems["content"]);
        }
        return new Dictionary<string, object> { { "exprs", exprs } };
    }

    public override Dictionary<string, object> VisitExpr(MetaPromptParser.ExprContext context)
    {
        var items = new List<object>();
        if (context.text() != null)
        {
            items.Add(VisitText(context.text()));
        }
        if (context.expr1() != null)
        {
            var expr1 = VisitExpr1(context.expr1());
            if ((string)expr1["type"] == "meta")
                items.Add(expr1["meta"]);
            else if ((string)expr1["type"] == "exprs")
            {
                items.Add(new Dictionary<string, object> { { "type", "text" }, { "text", "[" } });
                items.AddRange((IEnumerable<object>)expr1["exprs"]);
                items.Add(new Dictionary<string, object> { { "type", "text" }, { "text", "]" } });
            }
        }
        else
        {
            if (context.RB() != null)
                items.Add(new Dictionary<string, object> { { "type", "text" }, { "text", "]" } });
            if (context.LB() != null)
                items.Add(new Dictionary<string, object> { { "type", "text" }, { "text", "[" } });
        }
        return new Dictionary<string, object> { { "content", items } };
    }

    public override Dictionary<string, object> VisitExpr1(MetaPromptParser.Expr1Context context)
    {
        if (context.meta_body() != null)
            return new Dictionary<string, object> { { "type", "meta" }, { "meta", VisitMeta_body(context.meta_body()) } };
        else
            return new Dictionary<string, object> { { "type", "exprs" }, { "exprs", VisitExprs(context.exprs())["exprs"] } };
    }

    public override Dictionary<string, object> VisitMeta_body(MetaPromptParser.Meta_bodyContext context)
    {
        var exprsList = context.exprs();
        if (context.ELSE_KW() != null)
        {
            var conditionNode = VisitExprs(exprsList[0]);
            var thenNode = VisitExprs(exprsList[1]);
            var elseNode = VisitExprs(exprsList[2]);
            return new Dictionary<string, object>
            {
                { "type", "if_then_else" },
                { "condition", conditionNode },
                { "then", thenNode },
                { "else", elseNode }
            };
        }
        else if (context.IF_KW() != null)
        {
            var conditionNode = VisitExprs(exprsList[0]);
            var thenNode = VisitExprs(exprsList[1]);
            return new Dictionary<string, object>
            {
                { "type", "if_then_else" },
                { "condition", conditionNode },
                { "then", thenNode },
                { "else", new List<object>() }
            };
        }
        else if (context.VAR_NAME() != null)
        {
            string varName = context.VAR_NAME().GetText().Substring(1);
            if (context.EQ_KW() != null)
            {
                var exprs = new List<object>();
                foreach (var expr in context.exprs())
                {
                    var exprItems = VisitExprs(expr);
                    exprs.AddRange((IEnumerable<object>)exprItems["exprs"]);
                }
                return new Dictionary<string, object> { { "type", "assign" }, { "name", varName }, { "exprs", exprs } };
            }
            else
            {
                return new Dictionary<string, object> { { "type", "var" }, { "name", varName } };
            }
        }
        else if (context.META_KW() != null)
        {
            var exprs = new List<object>();
            foreach (var expr in context.exprs())
            {
                var exprItems = VisitExprs(expr);
                exprs.AddRange((IEnumerable<object>)exprItems["exprs"]);
            }
            return new Dictionary<string, object> { { "type", "meta" }, { "exprs", exprs } };
        }
        else
        {
            throw new Exception("Unable to build AST");
        }
    }

    public override Dictionary<string, object> VisitText(MetaPromptParser.TextContext context)
    {
        string text = string.Concat(context.CHAR().Select(c => c.GetText()));
        return new Dictionary<string, object> { { "type", "text" }, { "text", text } };
    }
}

