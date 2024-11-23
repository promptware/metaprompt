grammar MetaPrompt;

prompt:	exprs EOF ;
exprs: expr*? ;
exprs1: expr+? ;
expr: LB expr1 RB
    | text
    | RB
    | LB
    | COMMENT_KW
    | META_PROMPT
    | EQ_KW
    | VAR_NAME
    | CHOOSE_KW
    | OPTION_KW
    | DEFAULT_KW
    | IS_KW
    | CALL
    | WITH_KW
    ;

expr1
    : meta_body
    | exprs
    ;

meta_body
    : IF_KW exprs THEN_KW exprs ELSE_KW exprs
    | IF_KW exprs THEN_KW exprs
    | CHOOSE_KW exprs option+ default_option?
    | USE named_parameters
    | META_PROMPT exprs
    | COMMENT_KW exprs
    | var_assignment
    | var_optional_assignment
    | VAR_NAME
    | CALL call_arg1 call_arg*
    | CALL call_arg*
    ;

var_assignment
    : VAR_NAME EQ_KW exprs
    ;

var_optional_assignment
    : VAR_NAME EQ_OPTIONAL_KW exprs
    ;

call_arg1
    : var_assignment
    | exprs
    ;

call_arg
    : var_assignment
    | WITH_KW exprs
    ;

option
    : OPTION_KW exprs IS_KW exprs
    ;

default_option
    : DEFAULT_KW exprs
    ;

named_parameters
    : var_assignment*
    ;

text: CHAR+ ;

LB : '[';
RB : ']';
EQ_KW : '=' ;
EQ_OPTIONAL_KW : '?=' ;
META_PROMPT : [a-zA-Z_]?[a-zA-Z0-9_]* '$' ;
COMMENT_KW : '#' ;
CHAR : ( ESCAPED | .);
fragment ESCAPED : ESCAPE ESCAPEE;
fragment ESCAPEE : (LB | ESCAPE);
fragment ESCAPE : '\\';
USE : ':use' WS+ [a-zA-Z0-9/_.-]+ WS*;
CALL : '@' [a-zA-Z_][a-zA-Z0-9_]* WS*;
fragment WS : ' '|'\n';
IF_KW : ':if' ;
CHOOSE_KW : ':choose' ;
OPTION_KW : ':option' ;
WITH_KW : ':with' ;
DEFAULT_KW : ':default' ;
IS_KW : ':is' ;
THEN_KW : ':then' ;
ELSE_KW : ':else' ;
VAR_NAME : ':' [a-zA-Z_][a-zA-Z0-9_]* ;
