grammar MetaPrompt;

prompt:	exprs EOF ;
exprs: expr*? ;
expr: meta_body
    | text
    | EQ_KW
    | EQ_OPTIONAL_KW
    | OPTION_KW
    | WITH_KW
    | DEFAULT_KW
    | IS_KW
    | IF_KW
    | THEN_KW
    | ELSE_KW
    | VAR_NAME
    ;



meta_body
    : IF_KW exprs THEN_KW exprs ELSE_KW exprs RB
    | IF_KW exprs THEN_KW exprs RB
    | CHOOSE_KW exprs option+ default_option? RB
    | USE named_parameters RB
    | META_PROMPT exprs RB
    | COMMENT_KW exprs RB
    | LB var_assignment RB
    | var_optional_assignment
    | LB VAR_NAME RB
    | CALL call_arg1 call_arg* RB
    | CALL call_arg* RB
    ;

var_assignment
    : VAR_NAME EQ_KW exprs
    ;

var_optional_assignment
    : LB VAR_NAME EQ_OPTIONAL_KW exprs RB
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
META_PROMPT : LB [a-zA-Z_]?[a-zA-Z0-9_]* '$' ;
COMMENT_KW : LB '#' ;
CHAR : ( ESCAPED | .);
fragment ESCAPED : ESCAPE ESCAPEE;
fragment ESCAPEE : (LB | ESCAPE | RB);
fragment ESCAPE : '\\';
USE : LB ':use' WS+ [a-zA-Z0-9/_.-]+ WS*;
CALL : LB '@' [a-zA-Z_][a-zA-Z0-9_]* WS*;
fragment WS : ' '|'\n';
IF_KW : LB ':if' ;
CHOOSE_KW : LB ':choose' ;
OPTION_KW : ':option' ;
WITH_KW : ':with' ;
DEFAULT_KW : ':default' ;
IS_KW : ':is' ;
THEN_KW : ':then' ;
ELSE_KW : ':else' ;
VAR_NAME : ':' [a-zA-Z_][a-zA-Z0-9_]* ;
