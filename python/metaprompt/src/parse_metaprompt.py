import sys
from antlr4 import *
from parser.MetaPromptLexer import MetaPromptLexer
from parser.MetaPromptParser import MetaPromptParser
from parser.MetaPromptVisitor import MetaPromptVisitor
from antlr4.error.ErrorListener import ErrorListener


class ThrowingErrorListener(ErrorListener):
    """Custom error listener that raises exceptions on errors."""

    def __init__(self):
        super(ThrowingErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column} - {msg}")


class MetaPromptASTBuilder(MetaPromptVisitor):
    def visitPrompt(self, ctx: MetaPromptParser.PromptContext):
        exprs_node = self.visit(ctx.exprs())
        return {"type": "metaprompt", "exprs": exprs_node}

    def visitExprs(self, ctx: MetaPromptParser.ExprsContext):
        exprs = []
        for expr in ctx.expr():
            expr_items = self.visit(expr)
            exprs.extend(expr_items)
        return exprs

    def visitExpr(self, ctx: MetaPromptParser.ExprContext):
        items = []
        if ctx.text() is not None:
            items.append(self.visit(ctx.text()))
        if ctx.expr1() is not None:
            expr1 = self.visit(ctx.expr1())
            if expr1["type"] == "meta":
                items.append(expr1["meta"])
            elif expr1["type"] == "exprs":
                items.append({"type": "text", "text": "["})
                for child in expr1["exprs"]:
                    items.append(child)
                items.append({"type": "text", "text": "]"})
        else:
            if ctx.RB() is not None:
                items.append({"type": "text", "text": "]"})
            if ctx.LB() is not None:
                items.append({"type": "text", "text": "["})
        return items

    def visitExpr1(self, ctx: MetaPromptParser.Expr1Context):
        if ctx.meta_body() is not None:
            return {"type": "meta", "meta": self.visit(ctx.meta_body())}
        else:
            return {"type": "exprs", "exprs": self.visit(ctx.exprs())}

    def visitMeta_body(self, ctx: MetaPromptParser.Meta_bodyContext):
        exprs_list = ctx.exprs()
        if ctx.ELSE_KW() is not None:
            # IF_KW exprs THEN_KW exprs ELSE_KW exprs
            condition_node = self.visit(exprs_list[0])
            then_node = self.visit(exprs_list[1])
            else_node = self.visit(exprs_list[2])
            return {
                "type": "if_then_else",
                "condition": condition_node,
                "then": then_node,
                "else": else_node,
            }
        elif ctx.IF_KW() is not None:
            # IF_KW exprs THEN_KW exprs
            condition_node = self.visit(exprs_list[0])
            then_node = self.visit(exprs_list[1])
            return {
                "type": "if_then_else",
                "condition": condition_node,
                "then": then_node,
                "else": [],
            }
        elif ctx.VAR_NAME() is not None:
            var_name = ctx.VAR_NAME().getText()[1:]
            if ctx.EQ_KW() is not None:
                # [:var_name= value]
                exprs = []
                for expr in ctx.exprs():
                    expr_items = self.visit(expr)
                    exprs.extend(expr_items)
                return {"type": "assign", "name": var_name, "exprs": exprs}
            else:
                # slice the ":"
                return {"type": "var", "name": var_name}

        elif ctx.META_KW() is not None:
            # [$ exprs]
            exprs = []
            for expr in ctx.exprs():
                expr_items = self.visit(expr)
                exprs.extend(expr_items)
            return {"type": "meta", "exprs": exprs}
        else:
            raise ValueError("Unable to build AST:", ctx)

    def visitText(self, ctx: MetaPromptParser.TextContext):
        # text: CHAR+
        # Collect all CHAR tokens
        text = "".join([child.getText() for child in ctx.CHAR()])
        return {"type": "text", "text": text}


def extract_tokens(input_text):
    input_stream = InputStream(input_text)
    lexer = MetaPromptLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    tokens = []
    for token in token_stream.tokens:
        token_name = (
            MetaPromptLexer.symbolicNames[token.type]
            if hasattr(MetaPromptLexer, "symbolicNames")
            else str(token.type)
        )
        tokens.append(
            {
                "type": token_name,
                "text": token.text,
            }
        )

    return tokens


def parse_metaprompt(prompt):
    stream = InputStream(prompt)
    lexer = MetaPromptLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = MetaPromptParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())
    tree = parser.prompt()
    visitor = MetaPromptASTBuilder()
    ast = visitor.visit(tree)
    return ast
