grammar MetaPrompt;

prompt:	exprs EOF ;
exprs: expr*? ;
expr: LB expr1 RB
    | text
    | RB
    | LB
    ;

expr1
    : meta_body
    | exprs
    ;

meta_body
    : IF_KW exprs THEN_KW exprs ELSE_KW exprs
    | IF_KW exprs THEN_KW exprs
    | USE parameters?
    | META_KW exprs
    | VAR_NAME EQ_KW exprs
    | VAR_NAME
    ;

parameters
    : (VAR_NAME EQ_KW exprs)+
    ;

text: CHAR+ ;

LB : '[';
RB : ']';
EQ_KW : '=' ;
META_KW : '$' ;
CHAR : . ;
USE : ':use' WS+ [a-zA-Z0-9/_.-]+ WS*;
fragment WS : ' '|'\n';
IF_KW : ':if' ;
THEN_KW : ':then' ;
ELSE_KW : ':else' ;
VAR_NAME : ':' [a-zA-Z][a-zA-Z0-9]* ;
