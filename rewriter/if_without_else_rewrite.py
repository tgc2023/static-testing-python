from . rewriter import *

class IfWithoutElseTransformer(NodeTransformer):

    def visit_If(self, node: If):
        queue_nodes = [node]
        while len(queue_nodes) > 0:
            current_node = queue_nodes.pop(0)
            body_nodes = list(filter(lambda x: isinstance(x, If), current_node.body))
            orelse_nodes = list(filter(lambda x: isinstance(x, If), current_node.orelse))

            if len(current_node.orelse) == 1 and isinstance(current_node.orelse[0], Pass):
                current_node.orelse.pop()

            queue_nodes += body_nodes + orelse_nodes
            
        return node


class IfWithoutElseRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(IfWithoutElseTransformer().visit(ast))
        return new_tree