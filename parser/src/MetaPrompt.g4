grammar MetaPrompt;
prompt:	exprs EOF ;
exprs: expr* ;
expr: (text+? meta?)+
    ;
meta:   '[' meta_body ']'
    ;

meta_body
    : IF_KW exprs THEN_KW exprs ELSE_KW exprs
    | IF_KW exprs THEN_KW exprs
    ;

text: CHAR+;

CHAR : . ;
IF_KW : ':if' ;
THEN_KW : ':then' ;
ELSE_KW : ':else' ;
ESCAPED_CHAR : ESCAPE (SPECIAL_CHAR | ESCAPE_CHAR) ;
ESCAPE : '\\' ;
SPECIAL_CHAR : ']' | '[' | '\\' ;
ESCAPE_CHAR : '\\' ;
