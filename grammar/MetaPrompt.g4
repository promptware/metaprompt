grammar MetaPrompt;
prompt:	exprs EOF ;
exprs: expr* ;
expr: text? LB expr1
    | text
    | RB
    ;

expr1
    : meta_body RB
    | exprs
    ;

meta_body
    : IF_KW exprs THEN_KW exprs ELSE_KW exprs
    | IF_KW exprs THEN_KW exprs
    | META_KW exprs
    | VAR_NAME
    ;

text: CHAR+ ;

LB : '[';
RB : ']';
CHAR : . ;
IF_KW : ':if' ;
THEN_KW : ':then' ;
ELSE_KW : ':else' ;
META_KW : '$';
VAR_NAME : ':' [a-zA-Z][a-zA-Z0-9]* ;
