import sys
import re
from antlr4 import *
from parser.MetaPromptLexer import MetaPromptLexer
from parser.MetaPromptParser import MetaPromptParser
from parser.MetaPromptVisitor import MetaPromptVisitor
from antlr4.error.ErrorListener import ErrorListener


class ThrowingErrorListener(ErrorListener):
    """Custom error listener that raises exceptions on errors."""

    def __init__(self):
        super(ThrowingErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column} - {msg}")


_pattern = r"\\([\[\\])(\[)?"


def _escape_pattern(match):
    first = match.group(1)
    second = match.group(2)
    if second is None:
        if first == "\\":
            return "\\\\"
        elif first == "[":
            return "["
        else:
            raise ValueError("Invariant violation: _escape_pattern")
    else:
        return match.group(1)


def _process_escaping(string):
    return re.sub(_pattern, _escape_pattern, string)


def _join_text_pieces(children):
    """Joins multiple consequent text chunks into one:
    '[' 'foo' ']' -> '[foo]'
    (workaround for generated parser implementation details)
    """
    buf = None
    res = []
    for child in children:
        if buf is None:
            if child["type"] == "text":
                buf = child
            else:
                res.append(child)
        else:
            if child["type"] == "text":
                buf["text"] += child["text"]
            else:
                res.append(buf)
                buf = None
                res.append(child)
    if buf is not None:
        res.append(buf)
    return res


class MetaPromptASTBuilder(MetaPromptVisitor):
    def visitPrompt(self, ctx: MetaPromptParser.PromptContext):
        exprs_node = self.visit(ctx.exprs())
        return {"type": "metaprompt", "exprs": exprs_node}

    def visitExprs(self, ctx: MetaPromptParser.ExprsContext):
        exprs = []
        for expr in ctx.expr():
            expr_items = self.visit(expr)
            exprs.extend(expr_items)
        return _join_text_pieces(exprs)

    def visitExpr(self, ctx: MetaPromptParser.ExprContext):
        exprs = []
        if ctx.text() is not None:
            exprs.append(self.visit(ctx.text()))
        if ctx.expr1() is not None:
            expr1 = self.visit(ctx.expr1())
            if expr1["type"] == "meta":
                exprs.append(expr1["meta"])
            elif expr1["type"] == "exprs":
                exprs.append({"type": "text", "text": "["})
                for child in expr1["exprs"]:
                    exprs.append(child)
                exprs.append({"type": "text", "text": "]"})
        else:
            # a token is in a standalone position and should be
            # treaded as text
            for part in [
                ctx.RB(),
                ctx.LB(),
                ctx.COMMENT_KW(),
                ctx.META_PROMPT(),
                ctx.EQ_KW(),
                ctx.VAR_NAME(),
            ]:
                if part is not None:
                    exprs.append({"type": "text", "text": part.getText()})

        return _join_text_pieces(exprs)

    def visitExpr1(self, ctx: MetaPromptParser.Expr1Context):
        if ctx.meta_body() is not None:
            return {"type": "meta", "meta": self.visit(ctx.meta_body())}
        else:
            return {"type": "exprs", "exprs": self.visit(ctx.exprs())}

    def visitParameters(self, ctx: MetaPromptParser.ParametersContext):
        parameters = {}
        for name, exprs in zip(ctx.VAR_NAME(), ctx.exprs()):
            parameters[name.getText()[1:]] = self.visit(exprs)
        return parameters

    def visitMeta_body(self, ctx: MetaPromptParser.Meta_bodyContext):
        exprs_list = ctx.exprs()
        if ctx.ELSE_KW() is not None:
            # IF_KW exprs THEN_KW exprs ELSE_KW exprs
            condition_node = self.visit(exprs_list[0])
            then_node = self.visit(exprs_list[1])
            else_node = self.visit(exprs_list[2])
            return {
                "type": "if_then_else",
                "condition": condition_node,
                "then": then_node,
                "else": else_node,
            }
        elif ctx.IF_KW() is not None:
            # IF_KW exprs THEN_KW exprs
            condition_node = self.visit(exprs_list[0])
            then_node = self.visit(exprs_list[1])
            return {
                "type": "if_then_else",
                "condition": condition_node,
                "then": then_node,
                "else": [],
            }
        elif ctx.COMMENT_KW() is not None:
            exprs = self.visit(exprs_list[0])
            return {"type": "comment", "exprs": exprs}
        elif ctx.USE() is not None:
            module_name = ctx.USE().getText().removeprefix(":use").strip()
            parameters = {}
            if ctx.parameters() is not None:
                parameters = self.visit(ctx.parameters())
            return {
                "type": "use",
                "module_name": module_name,
                "parameters": parameters,
            }
        elif ctx.VAR_NAME() is not None:
            # slice the ":"
            var_name = ctx.VAR_NAME().getText()[1:]
            if ctx.EQ_KW() is not None:
                # [:var_name= value]
                exprs = []
                for expr in ctx.exprs():
                    expr_items = self.visit(expr)
                    exprs.extend(expr_items)
                return {
                    "type": "assign",
                    "name": var_name,
                    "exprs": _join_text_pieces(exprs),
                }
            else:
                return {"type": "var", "name": var_name}

        elif ctx.META_PROMPT() is not None:
            # [foo$ exprs]
            exprs = []
            for expr in ctx.exprs():
                expr_items = self.visit(expr)
                exprs.extend(expr_items)
            res = {
                "type": "meta",
                "exprs": _join_text_pieces(exprs),
            }
            chat_id = ctx.META_PROMPT().getText()[:-1]
            if chat_id != "":
                res["chat"] = chat_id
            return res

        else:
            raise ValueError("Unable to build AST:", ctx)

    def visitText(self, ctx: MetaPromptParser.TextContext):
        # text: CHAR+
        # Collect all CHAR tokens
        text = "".join(
            [_process_escaping(child.getText()) for child in ctx.CHAR()]
        )
        return {"type": "text", "text": text}


def extract_tokens(input_text):
    input_stream = InputStream(input_text)
    lexer = MetaPromptLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    tokens = []
    for token in token_stream.tokens:
        token_name = (
            MetaPromptLexer.symbolicNames[token.type]
            if hasattr(MetaPromptLexer, "symbolicNames")
            else str(token.type)
        )
        tokens.append(
            {
                "type": token_name,
                "text": token.text,
            }
        )

    return tokens


def parse_metaprompt(prompt):
    stream = InputStream(prompt)
    lexer = MetaPromptLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = MetaPromptParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())
    tree = parser.prompt()
    visitor = MetaPromptASTBuilder()
    ast = visitor.visit(tree)
    return ast
