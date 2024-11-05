import sys
from pprint import pprint
from antlr4 import *
from python_gen.src.MetaPromptLexer import MetaPromptLexer
from python_gen.src.MetaPromptParser import MetaPromptParser
from python_gen.src.MetaPromptVisitor import MetaPromptVisitor

class MetaPromptASTBuilder(MetaPromptVisitor):
    def visitPrompt(self, ctx: MetaPromptParser.PromptContext):
        exprs_node = self.visit(ctx.exprs())
        return {'type': 'Prompt', 'exprs': exprs_node}

    def visitExprs(self, ctx: MetaPromptParser.ExprsContext):
        exprs = [self.visit(expr) for expr in ctx.expr()]
        return exprs  # Return a list of expression nodes

    def visitExpr(self, ctx: MetaPromptParser.ExprContext):
        items = []
        # The expr rule is (text+? meta?)+
        # We need to process the sequence of text and meta

        # Since the group is repeated, we iterate over the children
        for child in ctx.getChildren():
            if isinstance(child, MetaPromptParser.TextContext):
                text_node = self.visit(child)
                items.append(text_node)
            elif isinstance(child, MetaPromptParser.MetaContext):
                meta_node = self.visit(child)
                items.append(meta_node)
            else:
                # Ignore other types (if any)
                pass

        return {'type': 'Expr', 'items': items}

    def visitMeta(self, ctx: MetaPromptParser.MetaContext):
        # meta: '[' meta_body ']'
        meta_body_node = self.visit(ctx.meta_body())
        return {'type': 'Meta', 'meta_body': meta_body_node}

    def visitMeta_body(self, ctx: MetaPromptParser.Meta_bodyContext):
        exprs_list = ctx.exprs()
        if ctx.ELSE_KW() is not None:
            # IF_KW exprs THEN_KW exprs ELSE_KW exprs
            condition_node = self.visit(exprs_list[0])
            then_node = self.visit(exprs_list[1])
            else_node = self.visit(exprs_list[2])
            return {
                'type': 'MetaBodyIfThenElse',
                'condition': condition_node,
                'then': then_node,
                'else': else_node
            }
        else:
            # IF_KW exprs THEN_KW exprs
            condition_node = self.visit(exprs_list[0])
            then_node = self.visit(exprs_list[1])
            return {
                'type': 'MetaBodyIfThen',
                'condition': condition_node,
                'then': then_node
            }

    def visitText(self, ctx: MetaPromptParser.TextContext):
        # text: CHAR+
        # Collect all CHAR tokens
        text = ''.join([child.getText() for child in ctx.getChildren()])
        return {'type': 'Text', 'text': text}

def parse_ast(prompt):
    stream = InputStream(prompt)
    lexer = MetaPromptLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = MetaPromptParser(stream)
    tree = parser.prompt()
    visitor = MetaPromptASTBuilder()
    ast = visitor.visit(tree)
    return ast

def main():
    prompt = 'asd [:if foo :then bar :else baz]'
    pprint(parse_ast(prompt), indent=2)
    # print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
