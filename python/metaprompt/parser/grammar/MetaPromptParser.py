# Generated from ./grammar/MetaPrompt.g4 by ANTLR 4.13.2
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
        4,1,9,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,3,2,23,8,2,1,2,1,2,1,2,1,
        2,3,2,29,8,2,1,3,1,3,1,3,1,3,3,3,35,8,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,55,8,4,1,5,4,
        5,58,8,5,11,5,12,5,59,1,5,0,0,6,0,2,4,6,8,10,0,0,65,0,12,1,0,0,0,
        2,18,1,0,0,0,4,28,1,0,0,0,6,34,1,0,0,0,8,54,1,0,0,0,10,57,1,0,0,
        0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,17,3,4,2,0,16,15,1,
        0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,0,20,
        18,1,0,0,0,21,23,3,10,5,0,22,21,1,0,0,0,22,23,1,0,0,0,23,24,1,0,
        0,0,24,25,5,1,0,0,25,29,3,6,3,0,26,29,3,10,5,0,27,29,5,2,0,0,28,
        22,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,0,29,5,1,0,0,0,30,31,3,8,4,
        0,31,32,5,2,0,0,32,35,1,0,0,0,33,35,3,2,1,0,34,30,1,0,0,0,34,33,
        1,0,0,0,35,7,1,0,0,0,36,37,5,6,0,0,37,38,3,2,1,0,38,39,5,7,0,0,39,
        40,3,2,1,0,40,41,5,8,0,0,41,42,3,2,1,0,42,55,1,0,0,0,43,44,5,6,0,
        0,44,45,3,2,1,0,45,46,5,7,0,0,46,47,3,2,1,0,47,55,1,0,0,0,48,49,
        5,4,0,0,49,55,3,2,1,0,50,51,5,9,0,0,51,52,5,3,0,0,52,55,3,2,1,0,
        53,55,5,9,0,0,54,36,1,0,0,0,54,43,1,0,0,0,54,48,1,0,0,0,54,50,1,
        0,0,0,54,53,1,0,0,0,55,9,1,0,0,0,56,58,5,5,0,0,57,56,1,0,0,0,58,
        59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,11,1,0,0,0,6,18,22,28,
        34,54,59
    ]

class MetaPromptParser ( Parser ):

    grammarFileName = "MetaPrompt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'='", "'$'", "<INVALID>", 
                     "':if'", "':then'", "':else'" ]

    symbolicNames = [ "<INVALID>", "LB", "RB", "EQ_KW", "META_KW", "CHAR", 
                      "IF_KW", "THEN_KW", "ELSE_KW", "VAR_NAME" ]

    RULE_prompt = 0
    RULE_exprs = 1
    RULE_expr = 2
    RULE_expr1 = 3
    RULE_meta_body = 4
    RULE_text = 5

    ruleNames =  [ "prompt", "exprs", "expr", "expr1", "meta_body", "text" ]

    EOF = Token.EOF
    LB=1
    RB=2
    EQ_KW=3
    META_KW=4
    CHAR=5
    IF_KW=6
    THEN_KW=7
    ELSE_KW=8
    VAR_NAME=9

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
            self.state = 12
            self.exprs()
            self.state = 13
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
            self.state = 18
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 15
                    self.expr() 
                self.state = 20
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


        def text(self):
            return self.getTypedRuleContext(MetaPromptParser.TextContext,0)


        def RB(self):
            return self.getToken(MetaPromptParser.RB, 0)

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
        self._la = 0 # Token type
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 21
                    self.text()


                self.state = 24
                self.match(MetaPromptParser.LB)
                self.state = 25
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.text()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(MetaPromptParser.RB)
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


        def RB(self):
            return self.getToken(MetaPromptParser.RB, 0)

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
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 6, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.meta_body()
                self.state = 31
                self.match(MetaPromptParser.RB)
                pass
            elif token in [-1, 1, 2, 5, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
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

        def META_KW(self):
            return self.getToken(MetaPromptParser.META_KW, 0)

        def VAR_NAME(self):
            return self.getToken(MetaPromptParser.VAR_NAME, 0)

        def EQ_KW(self):
            return self.getToken(MetaPromptParser.EQ_KW, 0)

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
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(MetaPromptParser.IF_KW)
                self.state = 37
                self.exprs()
                self.state = 38
                self.match(MetaPromptParser.THEN_KW)
                self.state = 39
                self.exprs()
                self.state = 40
                self.match(MetaPromptParser.ELSE_KW)
                self.state = 41
                self.exprs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(MetaPromptParser.IF_KW)
                self.state = 44
                self.exprs()
                self.state = 45
                self.match(MetaPromptParser.THEN_KW)
                self.state = 46
                self.exprs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(MetaPromptParser.META_KW)
                self.state = 49
                self.exprs()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(MetaPromptParser.VAR_NAME)
                self.state = 51
                self.match(MetaPromptParser.EQ_KW)
                self.state = 52
                self.exprs()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.match(MetaPromptParser.VAR_NAME)
                pass


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
        self.enterRule(localctx, 10, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 56
                    self.match(MetaPromptParser.CHAR)

                else:
                    raise NoViableAltException(self)
                self.state = 59 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





