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
        4,1,17,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,3,2,47,8,2,1,3,1,3,3,3,51,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,68,8,4,11,4,12,4,69,1,4,3,
        4,73,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,89,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,5,7,101,8,7,10,
        7,12,7,104,9,7,1,8,1,8,1,8,5,8,109,8,8,10,8,12,8,112,9,8,1,9,4,9,
        115,8,9,11,9,12,9,116,1,9,1,26,0,10,0,2,4,6,8,10,12,14,16,18,0,0,
        136,0,20,1,0,0,0,2,26,1,0,0,0,4,46,1,0,0,0,6,50,1,0,0,0,8,88,1,0,
        0,0,10,90,1,0,0,0,12,95,1,0,0,0,14,102,1,0,0,0,16,110,1,0,0,0,18,
        114,1,0,0,0,20,21,3,2,1,0,21,22,5,0,0,1,22,1,1,0,0,0,23,25,3,4,2,
        0,24,23,1,0,0,0,25,28,1,0,0,0,26,27,1,0,0,0,26,24,1,0,0,0,27,3,1,
        0,0,0,28,26,1,0,0,0,29,30,5,1,0,0,30,31,3,6,3,0,31,32,5,2,0,0,32,
        47,1,0,0,0,33,47,3,18,9,0,34,47,5,2,0,0,35,47,5,1,0,0,36,47,5,5,
        0,0,37,47,5,4,0,0,38,47,5,3,0,0,39,47,5,17,0,0,40,47,5,10,0,0,41,
        47,5,11,0,0,42,47,5,13,0,0,43,47,5,14,0,0,44,47,5,8,0,0,45,47,5,
        12,0,0,46,29,1,0,0,0,46,33,1,0,0,0,46,34,1,0,0,0,46,35,1,0,0,0,46,
        36,1,0,0,0,46,37,1,0,0,0,46,38,1,0,0,0,46,39,1,0,0,0,46,40,1,0,0,
        0,46,41,1,0,0,0,46,42,1,0,0,0,46,43,1,0,0,0,46,44,1,0,0,0,46,45,
        1,0,0,0,47,5,1,0,0,0,48,51,3,8,4,0,49,51,3,2,1,0,50,48,1,0,0,0,50,
        49,1,0,0,0,51,7,1,0,0,0,52,53,5,9,0,0,53,54,3,2,1,0,54,55,5,15,0,
        0,55,56,3,2,1,0,56,57,5,16,0,0,57,58,3,2,1,0,58,89,1,0,0,0,59,60,
        5,9,0,0,60,61,3,2,1,0,61,62,5,15,0,0,62,63,3,2,1,0,63,89,1,0,0,0,
        64,65,5,10,0,0,65,67,3,2,1,0,66,68,3,10,5,0,67,66,1,0,0,0,68,69,
        1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,73,3,12,6,0,
        72,71,1,0,0,0,72,73,1,0,0,0,73,89,1,0,0,0,74,75,5,7,0,0,75,89,3,
        16,8,0,76,77,5,4,0,0,77,89,3,2,1,0,78,79,5,5,0,0,79,89,3,2,1,0,80,
        81,5,17,0,0,81,82,5,3,0,0,82,89,3,2,1,0,83,89,5,17,0,0,84,85,5,8,
        0,0,85,86,3,14,7,0,86,87,3,16,8,0,87,89,1,0,0,0,88,52,1,0,0,0,88,
        59,1,0,0,0,88,64,1,0,0,0,88,74,1,0,0,0,88,76,1,0,0,0,88,78,1,0,0,
        0,88,80,1,0,0,0,88,83,1,0,0,0,88,84,1,0,0,0,89,9,1,0,0,0,90,91,5,
        11,0,0,91,92,3,2,1,0,92,93,5,14,0,0,93,94,3,2,1,0,94,11,1,0,0,0,
        95,96,5,13,0,0,96,97,3,2,1,0,97,13,1,0,0,0,98,99,5,12,0,0,99,101,
        3,2,1,0,100,98,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,
        0,0,0,103,15,1,0,0,0,104,102,1,0,0,0,105,106,5,17,0,0,106,107,5,
        3,0,0,107,109,3,2,1,0,108,105,1,0,0,0,109,112,1,0,0,0,110,108,1,
        0,0,0,110,111,1,0,0,0,111,17,1,0,0,0,112,110,1,0,0,0,113,115,5,6,
        0,0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,1,0,0,0,116,117,1,0,
        0,0,117,19,1,0,0,0,9,26,46,50,69,72,88,102,110,116
    ]

class MetaPromptParser ( Parser ):

    grammarFileName = "MetaPrompt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "<INVALID>", "<INVALID>", 
                     "'#'", "<INVALID>", "<INVALID>", "<INVALID>", "':if'", 
                     "':choose'", "':option'", "':with'", "':default'", 
                     "':is'", "':then'", "':else'" ]

    symbolicNames = [ "<INVALID>", "LB", "RB", "EQ_KW", "META_PROMPT", "COMMENT_KW", 
                      "CHAR", "USE", "CALL", "IF_KW", "CHOOSE_KW", "OPTION_KW", 
                      "WITH_KW", "DEFAULT_KW", "IS_KW", "THEN_KW", "ELSE_KW", 
                      "VAR_NAME" ]

    RULE_prompt = 0
    RULE_exprs = 1
    RULE_expr = 2
    RULE_expr1 = 3
    RULE_meta_body = 4
    RULE_option = 5
    RULE_default_option = 6
    RULE_positional_args = 7
    RULE_parameters = 8
    RULE_text = 9

    ruleNames =  [ "prompt", "exprs", "expr", "expr1", "meta_body", "option", 
                   "default_option", "positional_args", "parameters", "text" ]

    EOF = Token.EOF
    LB=1
    RB=2
    EQ_KW=3
    META_PROMPT=4
    COMMENT_KW=5
    CHAR=6
    USE=7
    CALL=8
    IF_KW=9
    CHOOSE_KW=10
    OPTION_KW=11
    WITH_KW=12
    DEFAULT_KW=13
    IS_KW=14
    THEN_KW=15
    ELSE_KW=16
    VAR_NAME=17

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
            self.state = 20
            self.exprs()
            self.state = 21
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
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 23
                    self.expr() 
                self.state = 28
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

        def LB(self):
            return self.getToken(MetaPromptParser.LB, 0)

        def expr1(self):
            return self.getTypedRuleContext(MetaPromptParser.Expr1Context,0)


        def RB(self):
            return self.getToken(MetaPromptParser.RB, 0)

        def text(self):
            return self.getTypedRuleContext(MetaPromptParser.TextContext,0)


        def COMMENT_KW(self):
            return self.getToken(MetaPromptParser.COMMENT_KW, 0)

        def META_PROMPT(self):
            return self.getToken(MetaPromptParser.META_PROMPT, 0)

        def EQ_KW(self):
            return self.getToken(MetaPromptParser.EQ_KW, 0)

        def VAR_NAME(self):
            return self.getToken(MetaPromptParser.VAR_NAME, 0)

        def CHOOSE_KW(self):
            return self.getToken(MetaPromptParser.CHOOSE_KW, 0)

        def OPTION_KW(self):
            return self.getToken(MetaPromptParser.OPTION_KW, 0)

        def DEFAULT_KW(self):
            return self.getToken(MetaPromptParser.DEFAULT_KW, 0)

        def IS_KW(self):
            return self.getToken(MetaPromptParser.IS_KW, 0)

        def CALL(self):
            return self.getToken(MetaPromptParser.CALL, 0)

        def WITH_KW(self):
            return self.getToken(MetaPromptParser.WITH_KW, 0)

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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(MetaPromptParser.LB)
                self.state = 30
                self.expr1()
                self.state = 31
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.text()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(MetaPromptParser.LB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.match(MetaPromptParser.COMMENT_KW)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 37
                self.match(MetaPromptParser.META_PROMPT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 38
                self.match(MetaPromptParser.EQ_KW)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 39
                self.match(MetaPromptParser.VAR_NAME)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 40
                self.match(MetaPromptParser.CHOOSE_KW)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 41
                self.match(MetaPromptParser.OPTION_KW)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 42
                self.match(MetaPromptParser.DEFAULT_KW)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 43
                self.match(MetaPromptParser.IS_KW)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 44
                self.match(MetaPromptParser.CALL)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 45
                self.match(MetaPromptParser.WITH_KW)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def meta_body(self):
            return self.getTypedRuleContext(MetaPromptParser.Meta_bodyContext,0)


        def exprs(self):
            return self.getTypedRuleContext(MetaPromptParser.ExprsContext,0)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_expr1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr1" ):
                listener.enterExpr1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr1" ):
                listener.exitExpr1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MetaPromptParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr1)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.meta_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.exprs()
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

        def parameters(self):
            return self.getTypedRuleContext(MetaPromptParser.ParametersContext,0)


        def META_PROMPT(self):
            return self.getToken(MetaPromptParser.META_PROMPT, 0)

        def COMMENT_KW(self):
            return self.getToken(MetaPromptParser.COMMENT_KW, 0)

        def VAR_NAME(self):
            return self.getToken(MetaPromptParser.VAR_NAME, 0)

        def EQ_KW(self):
            return self.getToken(MetaPromptParser.EQ_KW, 0)

        def CALL(self):
            return self.getToken(MetaPromptParser.CALL, 0)

        def positional_args(self):
            return self.getTypedRuleContext(MetaPromptParser.Positional_argsContext,0)


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
        self.enterRule(localctx, 8, self.RULE_meta_body)
        self._la = 0 # Token type
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(MetaPromptParser.IF_KW)
                self.state = 53
                self.exprs()
                self.state = 54
                self.match(MetaPromptParser.THEN_KW)
                self.state = 55
                self.exprs()
                self.state = 56
                self.match(MetaPromptParser.ELSE_KW)
                self.state = 57
                self.exprs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(MetaPromptParser.IF_KW)
                self.state = 60
                self.exprs()
                self.state = 61
                self.match(MetaPromptParser.THEN_KW)
                self.state = 62
                self.exprs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(MetaPromptParser.CHOOSE_KW)
                self.state = 65
                self.exprs()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 66
                    self.option()
                    self.state = 69 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==11):
                        break

                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 71
                    self.default_option()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.match(MetaPromptParser.USE)
                self.state = 75
                self.parameters()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.match(MetaPromptParser.META_PROMPT)
                self.state = 77
                self.exprs()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.match(MetaPromptParser.COMMENT_KW)
                self.state = 79
                self.exprs()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.match(MetaPromptParser.VAR_NAME)
                self.state = 81
                self.match(MetaPromptParser.EQ_KW)
                self.state = 82
                self.exprs()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.match(MetaPromptParser.VAR_NAME)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.match(MetaPromptParser.CALL)
                self.state = 85
                self.positional_args()
                self.state = 86
                self.parameters()
                pass


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
        self.enterRule(localctx, 10, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MetaPromptParser.OPTION_KW)
            self.state = 91
            self.exprs()
            self.state = 92
            self.match(MetaPromptParser.IS_KW)
            self.state = 93
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
        self.enterRule(localctx, 12, self.RULE_default_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(MetaPromptParser.DEFAULT_KW)
            self.state = 96
            self.exprs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Positional_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH_KW(self, i:int=None):
            if i is None:
                return self.getTokens(MetaPromptParser.WITH_KW)
            else:
                return self.getToken(MetaPromptParser.WITH_KW, i)

        def exprs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaPromptParser.ExprsContext)
            else:
                return self.getTypedRuleContext(MetaPromptParser.ExprsContext,i)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_positional_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositional_args" ):
                listener.enterPositional_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositional_args" ):
                listener.exitPositional_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositional_args" ):
                return visitor.visitPositional_args(self)
            else:
                return visitor.visitChildren(self)




    def positional_args(self):

        localctx = MetaPromptParser.Positional_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_positional_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 98
                self.match(MetaPromptParser.WITH_KW)
                self.state = 99
                self.exprs()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(MetaPromptParser.VAR_NAME)
            else:
                return self.getToken(MetaPromptParser.VAR_NAME, i)

        def EQ_KW(self, i:int=None):
            if i is None:
                return self.getTokens(MetaPromptParser.EQ_KW)
            else:
                return self.getToken(MetaPromptParser.EQ_KW, i)

        def exprs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaPromptParser.ExprsContext)
            else:
                return self.getTypedRuleContext(MetaPromptParser.ExprsContext,i)


        def getRuleIndex(self):
            return MetaPromptParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = MetaPromptParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 105
                self.match(MetaPromptParser.VAR_NAME)
                self.state = 106
                self.match(MetaPromptParser.EQ_KW)
                self.state = 107
                self.exprs()
                self.state = 112
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
        self.enterRule(localctx, 18, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 113
                    self.match(MetaPromptParser.CHAR)

                else:
                    raise NoViableAltException(self)
                self.state = 116 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





