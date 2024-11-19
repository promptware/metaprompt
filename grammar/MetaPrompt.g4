grammar MetaPrompt;

prompt:	exprs EOF ;
exprs: expr*? ;
expr: LB expr1 RB
    | text
    | RB
    | LB
    | COMMENT_KW
    | META_PROMPT
    | EQ_KW
    | VAR_NAME
    ;

expr1
    : meta_body
    | exprs
    ;

meta_body
    : IF_KW exprs THEN_KW exprs ELSE_KW exprs
    | IF_KW exprs THEN_KW exprs
    | USE parameters?
    | META_PROMPT exprs
    | COMMENT_KW exprs
    | VAR_NAME EQ_KW exprs
    | VAR_NAME
    ;

parameters
    : (VAR_NAME EQ_KW exprs)+
    ;

text: CHAR+ ;

LB : '[';
RB : ']';
EQ_KW : '=' | '?=' ;
META_PROMPT : [a-zA-Z_]?[a-zA-Z0-9_]* '$' ;
COMMENT_KW : '#' ;
CHAR : ( ESCAPED | .);
fragment ESCAPED : ESCAPE ESCAPEE;
fragment ESCAPEE : (LB | ESCAPE);
fragment ESCAPE : '\\';
USE : ':use' WS+ [a-zA-Z0-9/_.-]+ WS*;
fragment WS : ' '|'\n';
IF_KW : ':if' ;
THEN_KW : ':then' ;
ELSE_KW : ':else' ;
VAR_NAME : ':' [a-zA-Z_][a-zA-Z0-9_]* ;
