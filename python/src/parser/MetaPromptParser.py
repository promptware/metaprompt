# Generated from MetaPrompt.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,152,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,1,5,
        1,29,8,1,10,1,12,1,32,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,46,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,4,3,65,8,3,11,3,12,3,66,1,3,3,3,70,8,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,97,8,3,10,3,12,3,100,9,3,1,
        3,1,3,1,3,1,3,5,3,106,8,3,10,3,12,3,109,9,3,1,3,3,3,112,8,3,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,3,6,126,8,6,1,7,1,7,
        1,7,3,7,131,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,5,10,142,8,
        10,10,10,12,10,145,9,10,1,11,4,11,148,8,11,11,11,12,11,149,1,11,
        1,30,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,0,169,0,24,1,0,0,0,2,
        30,1,0,0,0,4,45,1,0,0,0,6,111,1,0,0,0,8,113,1,0,0,0,10,117,1,0,0,
        0,12,125,1,0,0,0,14,130,1,0,0,0,16,132,1,0,0,0,18,137,1,0,0,0,20,
        143,1,0,0,0,22,147,1,0,0,0,24,25,3,2,1,0,25,26,5,0,0,1,26,1,1,0,
        0,0,27,29,3,4,2,0,28,27,1,0,0,0,29,32,1,0,0,0,30,31,1,0,0,0,30,28,
        1,0,0,0,31,3,1,0,0,0,32,30,1,0,0,0,33,46,3,6,3,0,34,46,3,22,11,0,
        35,46,5,3,0,0,36,46,5,4,0,0,37,46,5,12,0,0,38,46,5,13,0,0,39,46,
        5,14,0,0,40,46,5,15,0,0,41,46,5,10,0,0,42,46,5,16,0,0,43,46,5,17,
        0,0,44,46,5,18,0,0,45,33,1,0,0,0,45,34,1,0,0,0,45,35,1,0,0,0,45,
        36,1,0,0,0,45,37,1,0,0,0,45,38,1,0,0,0,45,39,1,0,0,0,45,40,1,0,0,
        0,45,41,1,0,0,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,5,1,
        0,0,0,47,48,5,10,0,0,48,49,3,2,1,0,49,50,5,16,0,0,50,51,3,2,1,0,
        51,52,5,17,0,0,52,53,3,2,1,0,53,54,5,2,0,0,54,112,1,0,0,0,55,56,
        5,10,0,0,56,57,3,2,1,0,57,58,5,16,0,0,58,59,3,2,1,0,59,60,5,2,0,
        0,60,112,1,0,0,0,61,62,5,11,0,0,62,64,3,2,1,0,63,65,3,16,8,0,64,
        63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,
        0,68,70,3,18,9,0,69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,
        5,2,0,0,72,112,1,0,0,0,73,74,5,8,0,0,74,75,3,20,10,0,75,76,5,2,0,
        0,76,112,1,0,0,0,77,78,5,5,0,0,78,79,3,2,1,0,79,80,5,2,0,0,80,112,
        1,0,0,0,81,82,5,6,0,0,82,83,3,2,1,0,83,84,5,2,0,0,84,112,1,0,0,0,
        85,86,5,1,0,0,86,87,3,8,4,0,87,88,5,2,0,0,88,112,1,0,0,0,89,112,
        3,10,5,0,90,91,5,1,0,0,91,92,5,18,0,0,92,112,5,2,0,0,93,94,5,9,0,
        0,94,98,3,12,6,0,95,97,3,14,7,0,96,95,1,0,0,0,97,100,1,0,0,0,98,
        96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,5,
        2,0,0,102,112,1,0,0,0,103,107,5,9,0,0,104,106,3,14,7,0,105,104,1,
        0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,110,1,
        0,0,0,109,107,1,0,0,0,110,112,5,2,0,0,111,47,1,0,0,0,111,55,1,0,
        0,0,111,61,1,0,0,0,111,73,1,0,0,0,111,77,1,0,0,0,111,81,1,0,0,0,
        111,85,1,0,0,0,111,89,1,0,0,0,111,90,1,0,0,0,111,93,1,0,0,0,111,
        103,1,0,0,0,112,7,1,0,0,0,113,114,5,18,0,0,114,115,5,3,0,0,115,116,
        3,2,1,0,116,9,1,0,0,0,117,118,5,1,0,0,118,119,5,18,0,0,119,120,5,
        4,0,0,120,121,3,2,1,0,121,122,5,2,0,0,122,11,1,0,0,0,123,126,3,8,
        4,0,124,126,3,2,1,0,125,123,1,0,0,0,125,124,1,0,0,0,126,13,1,0,0,
        0,127,131,3,8,4,0,128,129,5,13,0,0,129,131,3,2,1,0,130,127,1,0,0,
        0,130,128,1,0,0,0,131,15,1,0,0,0,132,133,5,12,0,0,133,134,3,2,1,
        0,134,135,5,15,0,0,135,136,3,2,1,0,136,17,1,0,0,0,137,138,5,14,0,
        0,138,139,3,2,1,0,139,19,1,0,0,0,140,142,3,8,4,0,141,140,1,0,0,0,
        142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,21,1,0,0,0,145,
        143,1,0,0,0,146,148,5,7,0,0,147,146,1,0,0,0,148,149,1,0,0,0,149,
        147,1,0,0,0,149,150,1,0,0,0,150,23,1,0,0,0,11,30,45,66,69,98,107,
        111,125,130,143,149
    ]

class MetaPromptParser ( Parser ):

    grammarFileName = "MetaPrompt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'='", "'?='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "':option'", "':with'", "':default'", 
                     "':is'", "':then'", "':else'" ]

    symbolicNames = [ "<INVALID>", "LB", "RB", "EQ_KW", "EQ_OPTIONAL_KW", 
                      "META_PROMPT", "COMMENT_KW", "CHAR", "USE", "CALL", 
                      "IF_KW", "CHOOSE_KW", "OPTION_KW", "WITH_KW", "DEFAULT_KW", 
                      "IS_KW", "THEN_KW", "ELSE_KW", "VAR_NAME" ]

    RULE_prompt = 0
    RULE_exprs = 1
    RULE_expr = 2
    RULE_meta_body = 3
    RULE_var_assignment = 4
    RULE_var_optional_assignment = 5
    RULE_call_arg1 = 6
    RULE_call_arg = 7
    RULE_option = 8
    RULE_default_option = 9
    RULE_named_parameters = 10
    RULE_text = 11

    ruleNames =  [ "prompt", "exprs", "expr", "meta_body", "var_assignment", 
                   "var_optional_assignment", "call_arg1", "call_arg", "option", 
                   "default_option", "named_parameters", "text" ]

    EOF = Token.EOF
    LB=1
    RB=2
    EQ_KW=3
    EQ_OPTIONAL_KW=4
    META_PROMPT=5
    COMMENT_KW=6
    CHAR=7
    USE=8
    CALL=9
    IF_KW=10
    CHOOSE_KW=11
    OPTION_KW=12
    WITH_KW=13
    DEFAULT_KW=14
    IS_KW=15
    THEN_KW=16
    ELSE_KW=17
    VAR_NAME=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PromptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprs(self):
            return self.getTypedRuleContext(MetaPromptParser.ExprsContext,0)


        def EOF(self):
            return self.getToken(MetaPromptParser.EOF, 0)

        def getRuleIndex(self):
            return MetaPromptParser.RULE_prompt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrompt" ):
                listener.enterPrompt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrompt" ):
                listener.exitPrompt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrompt" ):
                return visitor.visitPrompt(self)
            else:
                return visitor.visitChildren(self)




    def prompt(self):

        localctx = MetaPromptParser.PromptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prompt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.exprs()
            self.state = 25
            self.match(MetaPromptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaPromptParser.ExprContext)
            else:
                return self.getTypedRuleContext(MetaPromptParser.ExprContext,i)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_exprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprs" ):
                listener.enterExprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprs" ):
                listener.exitExprs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = MetaPromptParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exprs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 27
                    self.expr() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def meta_body(self):
            return self.getTypedRuleContext(MetaPromptParser.Meta_bodyContext,0)


        def text(self):
            return self.getTypedRuleContext(MetaPromptParser.TextContext,0)


        def EQ_KW(self):
            return self.getToken(MetaPromptParser.EQ_KW, 0)

        def EQ_OPTIONAL_KW(self):
            return self.getToken(MetaPromptParser.EQ_OPTIONAL_KW, 0)

        def OPTION_KW(self):
            return self.getToken(MetaPromptParser.OPTION_KW, 0)

        def WITH_KW(self):
            return self.getToken(MetaPromptParser.WITH_KW, 0)

        def DEFAULT_KW(self):
            return self.getToken(MetaPromptParser.DEFAULT_KW, 0)

        def IS_KW(self):
            return self.getToken(MetaPromptParser.IS_KW, 0)

        def IF_KW(self):
            return self.getToken(MetaPromptParser.IF_KW, 0)

        def THEN_KW(self):
            return self.getToken(MetaPromptParser.THEN_KW, 0)

        def ELSE_KW(self):
            return self.getToken(MetaPromptParser.ELSE_KW, 0)

        def VAR_NAME(self):
            return self.getToken(MetaPromptParser.VAR_NAME, 0)

        def getRuleIndex(self):
            return MetaPromptParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MetaPromptParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.meta_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.text()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(MetaPromptParser.EQ_KW)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.match(MetaPromptParser.EQ_OPTIONAL_KW)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.match(MetaPromptParser.OPTION_KW)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 38
                self.match(MetaPromptParser.WITH_KW)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 39
                self.match(MetaPromptParser.DEFAULT_KW)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 40
                self.match(MetaPromptParser.IS_KW)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 41
                self.match(MetaPromptParser.IF_KW)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 42
                self.match(MetaPromptParser.THEN_KW)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 43
                self.match(MetaPromptParser.ELSE_KW)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 44
                self.match(MetaPromptParser.VAR_NAME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Meta_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KW(self):
            return self.getToken(MetaPromptParser.IF_KW, 0)

        def exprs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaPromptParser.ExprsContext)
            else:
                return self.getTypedRuleContext(MetaPromptParser.ExprsContext,i)


        def THEN_KW(self):
            return self.getToken(MetaPromptParser.THEN_KW, 0)

        def ELSE_KW(self):
            return self.getToken(MetaPromptParser.ELSE_KW, 0)

        def RB(self):
            return self.getToken(MetaPromptParser.RB, 0)

        def CHOOSE_KW(self):
            return self.getToken(MetaPromptParser.CHOOSE_KW, 0)

        def option(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaPromptParser.OptionContext)
            else:
                return self.getTypedRuleContext(MetaPromptParser.OptionContext,i)


        def default_option(self):
            return self.getTypedRuleContext(MetaPromptParser.Default_optionContext,0)


        def USE(self):
            return self.getToken(MetaPromptParser.USE, 0)

        def named_parameters(self):
            return self.getTypedRuleContext(MetaPromptParser.Named_parametersContext,0)


        def META_PROMPT(self):
            return self.getToken(MetaPromptParser.META_PROMPT, 0)

        def COMMENT_KW(self):
            return self.getToken(MetaPromptParser.COMMENT_KW, 0)

        def LB(self):
            return self.getToken(MetaPromptParser.LB, 0)

        def var_assignment(self):
            return self.getTypedRuleContext(MetaPromptParser.Var_assignmentContext,0)


        def var_optional_assignment(self):
            return self.getTypedRuleContext(MetaPromptParser.Var_optional_assignmentContext,0)


        def VAR_NAME(self):
            return self.getToken(MetaPromptParser.VAR_NAME, 0)

        def CALL(self):
            return self.getToken(MetaPromptParser.CALL, 0)

        def call_arg1(self):
            return self.getTypedRuleContext(MetaPromptParser.Call_arg1Context,0)


        def call_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaPromptParser.Call_argContext)
            else:
                return self.getTypedRuleContext(MetaPromptParser.Call_argContext,i)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_meta_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeta_body" ):
                listener.enterMeta_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeta_body" ):
                listener.exitMeta_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeta_body" ):
                return visitor.visitMeta_body(self)
            else:
                return visitor.visitChildren(self)




    def meta_body(self):

        localctx = MetaPromptParser.Meta_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_meta_body)
        self._la = 0 # Token type
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(MetaPromptParser.IF_KW)
                self.state = 48
                self.exprs()
                self.state = 49
                self.match(MetaPromptParser.THEN_KW)
                self.state = 50
                self.exprs()
                self.state = 51
                self.match(MetaPromptParser.ELSE_KW)
                self.state = 52
                self.exprs()
                self.state = 53
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(MetaPromptParser.IF_KW)
                self.state = 56
                self.exprs()
                self.state = 57
                self.match(MetaPromptParser.THEN_KW)
                self.state = 58
                self.exprs()
                self.state = 59
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(MetaPromptParser.CHOOSE_KW)
                self.state = 62
                self.exprs()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 63
                    self.option()
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==12):
                        break

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 68
                    self.default_option()


                self.state = 71
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.match(MetaPromptParser.USE)
                self.state = 74
                self.named_parameters()
                self.state = 75
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.match(MetaPromptParser.META_PROMPT)
                self.state = 78
                self.exprs()
                self.state = 79
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.match(MetaPromptParser.COMMENT_KW)
                self.state = 82
                self.exprs()
                self.state = 83
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 85
                self.match(MetaPromptParser.LB)
                self.state = 86
                self.var_assignment()
                self.state = 87
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 89
                self.var_optional_assignment()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 90
                self.match(MetaPromptParser.LB)
                self.state = 91
                self.match(MetaPromptParser.VAR_NAME)
                self.state = 92
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 93
                self.match(MetaPromptParser.CALL)
                self.state = 94
                self.call_arg1()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13 or _la==18:
                    self.state = 95
                    self.call_arg()
                    self.state = 100
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 101
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 103
                self.match(MetaPromptParser.CALL)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13 or _la==18:
                    self.state = 104
                    self.call_arg()
                    self.state = 109
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 110
                self.match(MetaPromptParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(MetaPromptParser.VAR_NAME, 0)

        def EQ_KW(self):
            return self.getToken(MetaPromptParser.EQ_KW, 0)

        def exprs(self):
            return self.getTypedRuleContext(MetaPromptParser.ExprsContext,0)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_var_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assignment" ):
                listener.enterVar_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assignment" ):
                listener.exitVar_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assignment" ):
                return visitor.visitVar_assignment(self)
            else:
                return visitor.visitChildren(self)




    def var_assignment(self):

        localctx = MetaPromptParser.Var_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MetaPromptParser.VAR_NAME)
            self.state = 114
            self.match(MetaPromptParser.EQ_KW)
            self.state = 115
            self.exprs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_optional_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MetaPromptParser.LB, 0)

        def VAR_NAME(self):
            return self.getToken(MetaPromptParser.VAR_NAME, 0)

        def EQ_OPTIONAL_KW(self):
            return self.getToken(MetaPromptParser.EQ_OPTIONAL_KW, 0)

        def exprs(self):
            return self.getTypedRuleContext(MetaPromptParser.ExprsContext,0)


        def RB(self):
            return self.getToken(MetaPromptParser.RB, 0)

        def getRuleIndex(self):
            return MetaPromptParser.RULE_var_optional_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_optional_assignment" ):
                listener.enterVar_optional_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_optional_assignment" ):
                listener.exitVar_optional_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_optional_assignment" ):
                return visitor.visitVar_optional_assignment(self)
            else:
                return visitor.visitChildren(self)




    def var_optional_assignment(self):

        localctx = MetaPromptParser.Var_optional_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_optional_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(MetaPromptParser.LB)
            self.state = 118
            self.match(MetaPromptParser.VAR_NAME)
            self.state = 119
            self.match(MetaPromptParser.EQ_OPTIONAL_KW)
            self.state = 120
            self.exprs()
            self.state = 121
            self.match(MetaPromptParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_arg1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_assignment(self):
            return self.getTypedRuleContext(MetaPromptParser.Var_assignmentContext,0)


        def exprs(self):
            return self.getTypedRuleContext(MetaPromptParser.ExprsContext,0)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_call_arg1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_arg1" ):
                listener.enterCall_arg1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_arg1" ):
                listener.exitCall_arg1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_arg1" ):
                return visitor.visitCall_arg1(self)
            else:
                return visitor.visitChildren(self)




    def call_arg1(self):

        localctx = MetaPromptParser.Call_arg1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_call_arg1)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.var_assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.exprs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_assignment(self):
            return self.getTypedRuleContext(MetaPromptParser.Var_assignmentContext,0)


        def WITH_KW(self):
            return self.getToken(MetaPromptParser.WITH_KW, 0)

        def exprs(self):
            return self.getTypedRuleContext(MetaPromptParser.ExprsContext,0)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_call_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_arg" ):
                listener.enterCall_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_arg" ):
                listener.exitCall_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_arg" ):
                return visitor.visitCall_arg(self)
            else:
                return visitor.visitChildren(self)




    def call_arg(self):

        localctx = MetaPromptParser.Call_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_call_arg)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.var_assignment()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(MetaPromptParser.WITH_KW)
                self.state = 129
                self.exprs()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTION_KW(self):
            return self.getToken(MetaPromptParser.OPTION_KW, 0)

        def exprs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaPromptParser.ExprsContext)
            else:
                return self.getTypedRuleContext(MetaPromptParser.ExprsContext,i)


        def IS_KW(self):
            return self.getToken(MetaPromptParser.IS_KW, 0)

        def getRuleIndex(self):
            return MetaPromptParser.RULE_option

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOption" ):
                listener.enterOption(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOption" ):
                listener.exitOption(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOption" ):
                return visitor.visitOption(self)
            else:
                return visitor.visitChildren(self)




    def option(self):

        localctx = MetaPromptParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(MetaPromptParser.OPTION_KW)
            self.state = 133
            self.exprs()
            self.state = 134
            self.match(MetaPromptParser.IS_KW)
            self.state = 135
            self.exprs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Default_optionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT_KW(self):
            return self.getToken(MetaPromptParser.DEFAULT_KW, 0)

        def exprs(self):
            return self.getTypedRuleContext(MetaPromptParser.ExprsContext,0)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_default_option

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault_option" ):
                listener.enterDefault_option(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault_option" ):
                listener.exitDefault_option(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefault_option" ):
                return visitor.visitDefault_option(self)
            else:
                return visitor.visitChildren(self)




    def default_option(self):

        localctx = MetaPromptParser.Default_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_default_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MetaPromptParser.DEFAULT_KW)
            self.state = 138
            self.exprs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Named_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaPromptParser.Var_assignmentContext)
            else:
                return self.getTypedRuleContext(MetaPromptParser.Var_assignmentContext,i)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_named_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamed_parameters" ):
                listener.enterNamed_parameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamed_parameters" ):
                listener.exitNamed_parameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamed_parameters" ):
                return visitor.visitNamed_parameters(self)
            else:
                return visitor.visitChildren(self)




    def named_parameters(self):

        localctx = MetaPromptParser.Named_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_named_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 140
                self.var_assignment()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(MetaPromptParser.CHAR)
            else:
                return self.getToken(MetaPromptParser.CHAR, i)

        def getRuleIndex(self):
            return MetaPromptParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = MetaPromptParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 146
                    self.match(MetaPromptParser.CHAR)

                else:
                    raise NoViableAltException(self)
                self.state = 149 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





