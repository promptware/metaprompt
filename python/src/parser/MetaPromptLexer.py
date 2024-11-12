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
        4,0,11,84,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,4,6,44,
        8,6,11,6,12,6,45,1,6,4,6,49,8,6,11,6,12,6,50,1,6,5,6,54,8,6,10,6,
        12,6,57,9,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,80,8,11,10,11,12,11,
        83,9,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,0,17,8,19,9,21,10,
        23,11,1,0,4,4,0,45,57,65,90,95,95,97,122,2,0,10,10,32,32,2,0,65,
        90,97,122,3,0,48,57,65,90,97,122,86,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,27,1,
        0,0,0,5,29,1,0,0,0,7,31,1,0,0,0,9,33,1,0,0,0,11,35,1,0,0,0,13,37,
        1,0,0,0,15,58,1,0,0,0,17,60,1,0,0,0,19,64,1,0,0,0,21,70,1,0,0,0,
        23,76,1,0,0,0,25,26,5,91,0,0,26,2,1,0,0,0,27,28,5,93,0,0,28,4,1,
        0,0,0,29,30,5,61,0,0,30,6,1,0,0,0,31,32,5,36,0,0,32,8,1,0,0,0,33,
        34,5,35,0,0,34,10,1,0,0,0,35,36,9,0,0,0,36,12,1,0,0,0,37,38,5,58,
        0,0,38,39,5,117,0,0,39,40,5,115,0,0,40,41,5,101,0,0,41,43,1,0,0,
        0,42,44,3,15,7,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,45,46,
        1,0,0,0,46,48,1,0,0,0,47,49,7,0,0,0,48,47,1,0,0,0,49,50,1,0,0,0,
        50,48,1,0,0,0,50,51,1,0,0,0,51,55,1,0,0,0,52,54,3,15,7,0,53,52,1,
        0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,14,1,0,0,0,57,
        55,1,0,0,0,58,59,7,1,0,0,59,16,1,0,0,0,60,61,5,58,0,0,61,62,5,105,
        0,0,62,63,5,102,0,0,63,18,1,0,0,0,64,65,5,58,0,0,65,66,5,116,0,0,
        66,67,5,104,0,0,67,68,5,101,0,0,68,69,5,110,0,0,69,20,1,0,0,0,70,
        71,5,58,0,0,71,72,5,101,0,0,72,73,5,108,0,0,73,74,5,115,0,0,74,75,
        5,101,0,0,75,22,1,0,0,0,76,77,5,58,0,0,77,81,7,2,0,0,78,80,7,3,0,
        0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,24,
        1,0,0,0,83,81,1,0,0,0,5,0,45,50,55,81,0
    ]

class MetaPromptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LB = 1
    RB = 2
    EQ_KW = 3
    META_KW = 4
    COMMENT_KW = 5
    CHAR = 6
    USE = 7
    IF_KW = 8
    THEN_KW = 9
    ELSE_KW = 10
    VAR_NAME = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'='", "'$'", "'#'", "':if'", "':then'", "':else'" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "EQ_KW", "META_KW", "COMMENT_KW", "CHAR", "USE", 
            "IF_KW", "THEN_KW", "ELSE_KW", "VAR_NAME" ]

    ruleNames = [ "LB", "RB", "EQ_KW", "META_KW", "COMMENT_KW", "CHAR", 
                  "USE", "WS", "IF_KW", "THEN_KW", "ELSE_KW", "VAR_NAME" ]

    grammarFileName = "MetaPrompt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


