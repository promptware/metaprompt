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
        4,0,10,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,3,6,47,8,6,1,7,1,7,1,8,1,8,1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,
        11,6,13,7,15,8,17,9,19,10,1,0,0,54,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,23,1,0,0,0,5,25,1,0,
        0,0,7,27,1,0,0,0,9,31,1,0,0,0,11,37,1,0,0,0,13,43,1,0,0,0,15,48,
        1,0,0,0,17,50,1,0,0,0,19,52,1,0,0,0,21,22,5,91,0,0,22,2,1,0,0,0,
        23,24,5,93,0,0,24,4,1,0,0,0,25,26,9,0,0,0,26,6,1,0,0,0,27,28,5,58,
        0,0,28,29,5,105,0,0,29,30,5,102,0,0,30,8,1,0,0,0,31,32,5,58,0,0,
        32,33,5,116,0,0,33,34,5,104,0,0,34,35,5,101,0,0,35,36,5,110,0,0,
        36,10,1,0,0,0,37,38,5,58,0,0,38,39,5,101,0,0,39,40,5,108,0,0,40,
        41,5,115,0,0,41,42,5,101,0,0,42,12,1,0,0,0,43,46,3,15,7,0,44,47,
        3,17,8,0,45,47,3,19,9,0,46,44,1,0,0,0,46,45,1,0,0,0,47,14,1,0,0,
        0,48,49,5,92,0,0,49,16,1,0,0,0,50,51,2,91,93,0,51,18,1,0,0,0,52,
        53,5,92,0,0,53,20,1,0,0,0,2,0,46,0
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
    ESCAPED_CHAR = 7
    ESCAPE = 8
    SPECIAL_CHAR = 9
    ESCAPE_CHAR = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "':if'", "':then'", "':else'" ]

    symbolicNames = [ "<INVALID>",
            "CHAR", "IF_KW", "THEN_KW", "ELSE_KW", "ESCAPED_CHAR", "ESCAPE", 
            "SPECIAL_CHAR", "ESCAPE_CHAR" ]

    ruleNames = [ "T__0", "T__1", "CHAR", "IF_KW", "THEN_KW", "ELSE_KW", 
                  "ESCAPED_CHAR", "ESCAPE", "SPECIAL_CHAR", "ESCAPE_CHAR" ]

    grammarFileName = "MetaPrompt.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


