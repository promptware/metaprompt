# Generated from MetaPrompt.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,53,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,5,8,49,8,8,10,8,12,8,52,9,8,0,0,9,1,1,3,2,5,3,7,4,9,5,
        11,6,13,7,15,8,17,9,1,0,2,2,0,65,90,97,122,3,0,48,57,65,90,97,122,
        53,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,
        21,1,0,0,0,5,23,1,0,0,0,7,25,1,0,0,0,9,27,1,0,0,0,11,29,1,0,0,0,
        13,33,1,0,0,0,15,39,1,0,0,0,17,45,1,0,0,0,19,20,5,91,0,0,20,2,1,
        0,0,0,21,22,5,93,0,0,22,4,1,0,0,0,23,24,5,61,0,0,24,6,1,0,0,0,25,
        26,5,36,0,0,26,8,1,0,0,0,27,28,9,0,0,0,28,10,1,0,0,0,29,30,5,58,
        0,0,30,31,5,105,0,0,31,32,5,102,0,0,32,12,1,0,0,0,33,34,5,58,0,0,
        34,35,5,116,0,0,35,36,5,104,0,0,36,37,5,101,0,0,37,38,5,110,0,0,
        38,14,1,0,0,0,39,40,5,58,0,0,40,41,5,101,0,0,41,42,5,108,0,0,42,
        43,5,115,0,0,43,44,5,101,0,0,44,16,1,0,0,0,45,46,5,58,0,0,46,50,
        7,0,0,0,47,49,7,1,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,
        50,51,1,0,0,0,51,18,1,0,0,0,52,50,1,0,0,0,2,0,50,0
    ]

class MetaPromptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LB = 1
    RB = 2
    EQ_KW = 3
    META_KW = 4
    CHAR = 5
    IF_KW = 6
    THEN_KW = 7
    ELSE_KW = 8
    VAR_NAME = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'='", "'$'", "':if'", "':then'", "':else'" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "EQ_KW", "META_KW", "CHAR", "IF_KW", "THEN_KW", 
            "ELSE_KW", "VAR_NAME" ]

    ruleNames = [ "LB", "RB", "EQ_KW", "META_KW", "CHAR", "IF_KW", "THEN_KW", 
                  "ELSE_KW", "VAR_NAME" ]

    grammarFileName = "MetaPrompt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


