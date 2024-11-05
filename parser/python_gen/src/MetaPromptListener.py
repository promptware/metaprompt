# Generated from src/MetaPrompt.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MetaPromptParser import MetaPromptParser
else:
    from MetaPromptParser import MetaPromptParser

# This class defines a complete listener for a parse tree produced by MetaPromptParser.
class MetaPromptListener(ParseTreeListener):

    # Enter a parse tree produced by MetaPromptParser#prompt.
    def enterPrompt(self, ctx:MetaPromptParser.PromptContext):
        pass

    # Exit a parse tree produced by MetaPromptParser#prompt.
    def exitPrompt(self, ctx:MetaPromptParser.PromptContext):
        pass


    # Enter a parse tree produced by MetaPromptParser#exprs.
    def enterExprs(self, ctx:MetaPromptParser.ExprsContext):
        pass

    # Exit a parse tree produced by MetaPromptParser#exprs.
    def exitExprs(self, ctx:MetaPromptParser.ExprsContext):
        pass


    # Enter a parse tree produced by MetaPromptParser#expr.
    def enterExpr(self, ctx:MetaPromptParser.ExprContext):
        pass

    # Exit a parse tree produced by MetaPromptParser#expr.
    def exitExpr(self, ctx:MetaPromptParser.ExprContext):
        pass


    # Enter a parse tree produced by MetaPromptParser#meta.
    def enterMeta(self, ctx:MetaPromptParser.MetaContext):
        pass

    # Exit a parse tree produced by MetaPromptParser#meta.
    def exitMeta(self, ctx:MetaPromptParser.MetaContext):
        pass


    # Enter a parse tree produced by MetaPromptParser#meta_body.
    def enterMeta_body(self, ctx:MetaPromptParser.Meta_bodyContext):
        pass

    # Exit a parse tree produced by MetaPromptParser#meta_body.
    def exitMeta_body(self, ctx:MetaPromptParser.Meta_bodyContext):
        pass


    # Enter a parse tree produced by MetaPromptParser#text.
    def enterText(self, ctx:MetaPromptParser.TextContext):
        pass

    # Exit a parse tree produced by MetaPromptParser#text.
    def exitText(self, ctx:MetaPromptParser.TextContext):
        pass



del MetaPromptParser