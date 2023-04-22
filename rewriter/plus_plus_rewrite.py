from . rewriter import *

class PlussPlussTransformer(NodeTransformer):

    def visit_Assign(self, node: Assign):
        statements = node
        target = node.targets[0]
        value  = node.value
        if not isinstance(value, BinOp):
            return statements

        if isinstance(target, Name):
            if isinstance(value.left, Name) and target.id == value.left.id:
                statements = AugAssign(target, value.op, value.right)
        
        elif isinstance(target, Attribute) and isinstance(target.value, Name):
            if isinstance(value.left, Attribute) and isinstance(value.left.value, Name):
                if target.value.id == value.left.value.id and target.attr == value.left.attr:
                    statements = AugAssign(target, value.op, value.right)
        
        return statements


class PlussPlussRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(PlussPlussTransformer().visit(ast))
        return new_tree
