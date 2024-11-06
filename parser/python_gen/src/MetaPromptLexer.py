# Generated from src/MetaPrompt.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,45,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,41,8,6,10,6,12,6,44,
        9,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,2,2,0,65,90,97,122,3,
        0,48,57,65,90,97,122,45,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,
        1,0,0,0,5,19,1,0,0,0,7,21,1,0,0,0,9,25,1,0,0,0,11,31,1,0,0,0,13,
        37,1,0,0,0,15,16,5,91,0,0,16,2,1,0,0,0,17,18,5,93,0,0,18,4,1,0,0,
        0,19,20,9,0,0,0,20,6,1,0,0,0,21,22,5,58,0,0,22,23,5,105,0,0,23,24,
        5,102,0,0,24,8,1,0,0,0,25,26,5,58,0,0,26,27,5,116,0,0,27,28,5,104,
        0,0,28,29,5,101,0,0,29,30,5,110,0,0,30,10,1,0,0,0,31,32,5,58,0,0,
        32,33,5,101,0,0,33,34,5,108,0,0,34,35,5,115,0,0,35,36,5,101,0,0,
        36,12,1,0,0,0,37,38,5,58,0,0,38,42,7,0,0,0,39,41,7,1,0,0,40,39,1,
        0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,14,1,0,0,0,44,
        42,1,0,0,0,2,0,42,0
    ]

class MetaPromptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    CHAR = 3
    IF_KW = 4
    THEN_KW = 5
    ELSE_KW = 6
    VAR_NAME = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "':if'", "':then'", "':else'" ]

    symbolicNames = [ "<INVALID>",
            "CHAR", "IF_KW", "THEN_KW", "ELSE_KW", "VAR_NAME" ]

    ruleNames = [ "T__0", "T__1", "CHAR", "IF_KW", "THEN_KW", "ELSE_KW", 
                  "VAR_NAME" ]

    grammarFileName = "MetaPrompt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


