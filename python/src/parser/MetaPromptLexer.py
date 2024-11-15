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
        4,0,11,101,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,
        5,3,5,44,8,5,1,6,1,6,1,6,1,7,1,7,3,7,51,8,7,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,4,9,61,8,9,11,9,12,9,62,1,9,4,9,66,8,9,11,9,12,9,67,
        1,9,5,9,71,8,9,10,9,12,9,74,9,9,1,10,1,10,1,11,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,5,14,97,8,14,10,14,12,14,100,9,14,0,0,15,1,1,3,2,5,3,7,4,
        9,5,11,6,13,0,15,0,17,0,19,7,21,0,23,8,25,9,27,10,29,11,1,0,4,4,
        0,45,57,65,90,95,95,97,122,2,0,10,10,32,32,2,0,65,90,97,122,3,0,
        48,57,65,90,97,122,102,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,19,1,0,0,0,0,23,1,0,0,0,0,25,1,
        0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,1,31,1,0,0,0,3,33,1,0,0,0,5,35,1,
        0,0,0,7,37,1,0,0,0,9,39,1,0,0,0,11,43,1,0,0,0,13,45,1,0,0,0,15,50,
        1,0,0,0,17,52,1,0,0,0,19,54,1,0,0,0,21,75,1,0,0,0,23,77,1,0,0,0,
        25,81,1,0,0,0,27,87,1,0,0,0,29,93,1,0,0,0,31,32,5,91,0,0,32,2,1,
        0,0,0,33,34,5,93,0,0,34,4,1,0,0,0,35,36,5,61,0,0,36,6,1,0,0,0,37,
        38,5,36,0,0,38,8,1,0,0,0,39,40,5,35,0,0,40,10,1,0,0,0,41,44,3,13,
        6,0,42,44,9,0,0,0,43,41,1,0,0,0,43,42,1,0,0,0,44,12,1,0,0,0,45,46,
        3,17,8,0,46,47,3,15,7,0,47,14,1,0,0,0,48,51,3,1,0,0,49,51,3,17,8,
        0,50,48,1,0,0,0,50,49,1,0,0,0,51,16,1,0,0,0,52,53,5,92,0,0,53,18,
        1,0,0,0,54,55,5,58,0,0,55,56,5,117,0,0,56,57,5,115,0,0,57,58,5,101,
        0,0,58,60,1,0,0,0,59,61,3,21,10,0,60,59,1,0,0,0,61,62,1,0,0,0,62,
        60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,66,7,0,0,0,65,64,1,0,0,
        0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,72,1,0,0,0,69,71,
        3,21,10,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,
        0,73,20,1,0,0,0,74,72,1,0,0,0,75,76,7,1,0,0,76,22,1,0,0,0,77,78,
        5,58,0,0,78,79,5,105,0,0,79,80,5,102,0,0,80,24,1,0,0,0,81,82,5,58,
        0,0,82,83,5,116,0,0,83,84,5,104,0,0,84,85,5,101,0,0,85,86,5,110,
        0,0,86,26,1,0,0,0,87,88,5,58,0,0,88,89,5,101,0,0,89,90,5,108,0,0,
        90,91,5,115,0,0,91,92,5,101,0,0,92,28,1,0,0,0,93,94,5,58,0,0,94,
        98,7,2,0,0,95,97,7,3,0,0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,0,
        0,0,98,99,1,0,0,0,99,30,1,0,0,0,100,98,1,0,0,0,7,0,43,50,62,67,72,
        98,0
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
                  "ESCAPED", "ESCAPEE", "ESCAPE", "USE", "WS", "IF_KW", 
                  "THEN_KW", "ELSE_KW", "VAR_NAME" ]

    grammarFileName = "MetaPrompt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


