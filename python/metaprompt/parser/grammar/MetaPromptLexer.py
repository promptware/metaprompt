# Generated from ./grammar/MetaPrompt.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,45,
        8,7,10,7,12,7,48,9,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,
        0,2,2,0,65,90,97,122,3,0,48,57,65,90,97,122,49,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,19,1,0,0,0,5,21,1,0,0,0,7,23,1,0,
        0,0,9,27,1,0,0,0,11,33,1,0,0,0,13,39,1,0,0,0,15,41,1,0,0,0,17,18,
        5,91,0,0,18,2,1,0,0,0,19,20,5,93,0,0,20,4,1,0,0,0,21,22,9,0,0,0,
        22,6,1,0,0,0,23,24,5,58,0,0,24,25,5,105,0,0,25,26,5,102,0,0,26,8,
        1,0,0,0,27,28,5,58,0,0,28,29,5,116,0,0,29,30,5,104,0,0,30,31,5,101,
        0,0,31,32,5,110,0,0,32,10,1,0,0,0,33,34,5,58,0,0,34,35,5,101,0,0,
        35,36,5,108,0,0,36,37,5,115,0,0,37,38,5,101,0,0,38,12,1,0,0,0,39,
        40,5,36,0,0,40,14,1,0,0,0,41,42,5,58,0,0,42,46,7,0,0,0,43,45,7,1,
        0,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,16,
        1,0,0,0,48,46,1,0,0,0,2,0,46,0
    ]

class MetaPromptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LB = 1
    RB = 2
    CHAR = 3
    IF_KW = 4
    THEN_KW = 5
    ELSE_KW = 6
    META_KW = 7
    VAR_NAME = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "':if'", "':then'", "':else'", "'$'" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "CHAR", "IF_KW", "THEN_KW", "ELSE_KW", "META_KW", 
            "VAR_NAME" ]

    ruleNames = [ "LB", "RB", "CHAR", "IF_KW", "THEN_KW", "ELSE_KW", "META_KW", 
                  "VAR_NAME" ]

    grammarFileName = "MetaPrompt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


