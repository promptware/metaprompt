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


    # Visit a parse tree produced by MetaPromptParser#meta_body.
    def visitMeta_body(self, ctx:MetaPromptParser.Meta_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#var_assignment.
    def visitVar_assignment(self, ctx:MetaPromptParser.Var_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#var_optional_assignment.
    def visitVar_optional_assignment(self, ctx:MetaPromptParser.Var_optional_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#call_arg1.
    def visitCall_arg1(self, ctx:MetaPromptParser.Call_arg1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#call_arg.
    def visitCall_arg(self, ctx:MetaPromptParser.Call_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#option.
    def visitOption(self, ctx:MetaPromptParser.OptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#default_option.
    def visitDefault_option(self, ctx:MetaPromptParser.Default_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#named_parameters.
    def visitNamed_parameters(self, ctx:MetaPromptParser.Named_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaPromptParser#text.
    def visitText(self, ctx:MetaPromptParser.TextContext):
        return self.visitChildren(ctx)



del MetaPromptParser