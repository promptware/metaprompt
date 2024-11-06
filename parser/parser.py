import sys
from antlr4 import *
from python_gen.src.MetaPromptLexer import MetaPromptLexer
from python_gen.src.MetaPromptParser import MetaPromptParser
from python_gen.src.MetaPromptVisitor import MetaPromptVisitor
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
        # The 'expr' rule is (text+? meta?)+, so we iterate over the children
        for child in ctx.getChildren():
            if isinstance(child, MetaPromptParser.TextContext):
                text_node = self.visit(child)
                items.append(text_node)
            elif isinstance(child, MetaPromptParser.MetaContext):
                meta_node = self.visit(child)
                items.append(meta_node)
            else:
                # Ignore other types if any
                pass
        return items

    def visitMeta(self, ctx: MetaPromptParser.MetaContext):
        # meta: '[' meta_body ']'
        meta_body_node = self.visit(ctx.meta_body())
        return meta_body_node

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
            return {"type": "if_then", "condition": condition_node, "then": then_node}
        elif ctx.META_KW() is not None:
            # [$ exprs]
            exprs_node = self.visit(ctx.exprs())
            return {"type": "meta", "exprs": exprs_node}
        elif ctx.VAR_NAME() is not None:
            var_name = ctx.VAR_NAME().getText()[1:]
            # slice the ":"
            return {"type": "var", "name": var_name}
        elif ctx.exprs() is not None:
            exprs = self.visit(exprs_list[0])
            return {"type": "brackets", "exprs": exprs}
        else:
            raise ValueError("Unable to build AST:", ctx)

    def visitText(self, ctx: MetaPromptParser.TextContext):
        # text: CHAR+
        # Collect all CHAR tokens
        text = "".join([child.getText() for child in ctx.CHAR()])
        return {"type": "text", "text": text}


def parse_ast(prompt):
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
