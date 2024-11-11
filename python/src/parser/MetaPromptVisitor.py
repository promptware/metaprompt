# Generated from MetaPrompt.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MetaPromptParser import MetaPromptParser
else:
    from MetaPromptParser import MetaPromptParser

# This class defines a complete generic visitor for a parse tree produced by MetaPromptParser.

class MetaPromptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MetaPromptParser#prompt.
    def visitPrompt(self, ctx:MetaPromptParser.PromptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#exprs.
    def visitExprs(self, ctx:MetaPromptParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#expr.
    def visitExpr(self, ctx:MetaPromptParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#expr1.
    def visitExpr1(self, ctx:MetaPromptParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#meta_body.
    def visitMeta_body(self, ctx:MetaPromptParser.Meta_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#parameters.
    def visitParameters(self, ctx:MetaPromptParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#text.
    def visitText(self, ctx:MetaPromptParser.TextContext):
        return self.visitChildren(ctx)



del MetaPromptParser