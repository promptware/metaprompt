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
        4,1,11,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,32,8,2,1,3,1,3,3,3,36,8,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,62,8,4,1,5,1,5,1,5,4,5,67,8,5,11,5,12,5,68,1,6,
        4,6,72,8,6,11,6,12,6,73,1,6,1,20,0,7,0,2,4,6,8,10,12,0,0,83,0,14,
        1,0,0,0,2,20,1,0,0,0,4,31,1,0,0,0,6,35,1,0,0,0,8,61,1,0,0,0,10,66,
        1,0,0,0,12,71,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,
        19,3,4,2,0,18,17,1,0,0,0,19,22,1,0,0,0,20,21,1,0,0,0,20,18,1,0,0,
        0,21,3,1,0,0,0,22,20,1,0,0,0,23,24,5,1,0,0,24,25,3,6,3,0,25,26,5,
        2,0,0,26,32,1,0,0,0,27,32,3,12,6,0,28,32,5,2,0,0,29,32,5,1,0,0,30,
        32,5,5,0,0,31,23,1,0,0,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,1,0,0,
        0,31,30,1,0,0,0,32,5,1,0,0,0,33,36,3,8,4,0,34,36,3,2,1,0,35,33,1,
        0,0,0,35,34,1,0,0,0,36,7,1,0,0,0,37,38,5,8,0,0,38,39,3,2,1,0,39,
        40,5,9,0,0,40,41,3,2,1,0,41,42,5,10,0,0,42,43,3,2,1,0,43,62,1,0,
        0,0,44,45,5,8,0,0,45,46,3,2,1,0,46,47,5,9,0,0,47,48,3,2,1,0,48,62,
        1,0,0,0,49,51,5,7,0,0,50,52,3,10,5,0,51,50,1,0,0,0,51,52,1,0,0,0,
        52,62,1,0,0,0,53,54,5,4,0,0,54,62,3,2,1,0,55,56,5,5,0,0,56,62,3,
        2,1,0,57,58,5,11,0,0,58,59,5,3,0,0,59,62,3,2,1,0,60,62,5,11,0,0,
        61,37,1,0,0,0,61,44,1,0,0,0,61,49,1,0,0,0,61,53,1,0,0,0,61,55,1,
        0,0,0,61,57,1,0,0,0,61,60,1,0,0,0,62,9,1,0,0,0,63,64,5,11,0,0,64,
        65,5,3,0,0,65,67,3,2,1,0,66,63,1,0,0,0,67,68,1,0,0,0,68,66,1,0,0,
        0,68,69,1,0,0,0,69,11,1,0,0,0,70,72,5,6,0,0,71,70,1,0,0,0,72,73,
        1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,13,1,0,0,0,7,20,31,35,51,
        61,68,73
    ]

class MetaPromptParser ( Parser ):

    grammarFileName = "MetaPrompt.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'='", "'$'", "'#'", "<INVALID>", 
                     "<INVALID>", "':if'", "':then'", "':else'" ]

    symbolicNames = [ "<INVALID>", "LB", "RB", "EQ_KW", "META_KW", "COMMENT_KW", 
                      "CHAR", "USE", "IF_KW", "THEN_KW", "ELSE_KW", "VAR_NAME" ]

    RULE_prompt = 0
    RULE_exprs = 1
    RULE_expr = 2
    RULE_expr1 = 3
    RULE_meta_body = 4
    RULE_parameters = 5
    RULE_text = 6

    ruleNames =  [ "prompt", "exprs", "expr", "expr1", "meta_body", "parameters", 
                   "text" ]

    EOF = Token.EOF
    LB=1
    RB=2
    EQ_KW=3
    META_KW=4
    COMMENT_KW=5
    CHAR=6
    USE=7
    IF_KW=8
    THEN_KW=9
    ELSE_KW=10
    VAR_NAME=11

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
            self.state = 14
            self.exprs()
            self.state = 15
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
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 17
                    self.expr() 
                self.state = 22
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
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(MetaPromptParser.LB)
                self.state = 24
                self.expr1()
                self.state = 25
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.text()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(MetaPromptParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.match(MetaPromptParser.LB)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.match(MetaPromptParser.COMMENT_KW)
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
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.meta_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
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

        def USE(self):
            return self.getToken(MetaPromptParser.USE, 0)

        def parameters(self):
            return self.getTypedRuleContext(MetaPromptParser.ParametersContext,0)


        def META_KW(self):
            return self.getToken(MetaPromptParser.META_KW, 0)

        def COMMENT_KW(self):
            return self.getToken(MetaPromptParser.COMMENT_KW, 0)

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
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(MetaPromptParser.IF_KW)
                self.state = 38
                self.exprs()
                self.state = 39
                self.match(MetaPromptParser.THEN_KW)
                self.state = 40
                self.exprs()
                self.state = 41
                self.match(MetaPromptParser.ELSE_KW)
                self.state = 42
                self.exprs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(MetaPromptParser.IF_KW)
                self.state = 45
                self.exprs()
                self.state = 46
                self.match(MetaPromptParser.THEN_KW)
                self.state = 47
                self.exprs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(MetaPromptParser.USE)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 50
                    self.parameters()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.match(MetaPromptParser.META_KW)
                self.state = 54
                self.exprs()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.match(MetaPromptParser.COMMENT_KW)
                self.state = 56
                self.exprs()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.match(MetaPromptParser.VAR_NAME)
                self.state = 58
                self.match(MetaPromptParser.EQ_KW)
                self.state = 59
                self.exprs()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.match(MetaPromptParser.VAR_NAME)
                pass


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
        self.enterRule(localctx, 10, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.match(MetaPromptParser.VAR_NAME)
                self.state = 64
                self.match(MetaPromptParser.EQ_KW)
                self.state = 65
                self.exprs()
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11):
                    break

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
        self.enterRule(localctx, 12, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 70
                    self.match(MetaPromptParser.CHAR)

                else:
                    raise NoViableAltException(self)
                self.state = 73 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




