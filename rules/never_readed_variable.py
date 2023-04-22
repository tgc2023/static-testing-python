from . rule import *

class AssignVisitor(WarningNodeVisitor):
    def __init__(self, len_nodes, tree_file):
        super().__init__()
        self.repeats = dict()
        self.counter_nodes = 0
        self.len_nodes = len_nodes
        self.tree_file = tree_file
    
    def add_repeats(self, id, lineno):
        if id in self.repeats.keys():
            self.repeats[id]['counter'] += 1
        else:
            self.repeats[id] = dict()
            self.repeats[id]['counter'] = 0
            self.repeats[id]['line'] = lineno
    
    def manage_warning(self, node):
        for key, value in self.repeats.items():
            if value['counter']== 0:
                self.tree_file.addWarning('NeverReadedVariable', value['line'], 'attribute ' + key + ' this variable was initialized but never used!!')


    def visit_Assign(self, node: Assign):
        #si es una variable temporal
        if isinstance(node.targets[0], Name):
            self.counter_nodes += 1
            self.add_repeats(node.targets[0].id, node.lineno)
            if self.counter_nodes == self.len_nodes:
                self.manage_warning(node)
        NodeVisitor.generic_visit(self, node)

    def visit_BinOp(self, node: BinOp):
        if isinstance(node.left, Name):
            self.add_repeats(node.left.id, node.lineno)
            if self.counter_nodes == self.len_nodes:
                self.manage_warning(node)
        if isinstance(node.right, Name):
            self.add_repeats(node.right.id, node.lineno)
            if self.counter_nodes == self.len_nodes:
                self.manage_warning(node)

    def visit_Return(self, node: Return):
        self.counter_nodes += 1
        if isinstance(node.value, BinOp):
            if isinstance(node.value.left, Name):
                self.add_repeats(node.value.left.id, node.lineno)
            if isinstance(node.value.right, Name):
                self.add_repeats(node.value.right.id, node.lineno)
            if self.counter_nodes == self.len_nodes:
                    self.manage_warning(node)
        elif isinstance(node.value, Name):
            self.add_repeats(node.value.id, node.lineno)
            if self.counter_nodes == self.len_nodes:
                    self.manage_warning(node)
        
    
    #falta revisar nodos Returns

class FunctionsVisitor(WarningNodeVisitor):
    def __init__(self, ast):
        super().__init__()
        self.repeats = dict()
        self.ast = ast

    def visit_FunctionDef(self, node: FunctionDef):
        node_return = 1 if 'Return' in dump(node)  else 0
        total_len_node_function = len(node.body) + node_return
        visitor = AssignVisitor(len(node.body), self)
        ast_function= parse(node)
        visitor.visit(ast_function)
        NodeVisitor.generic_visit(self, node)


class NeverReadedVariable(Rule):
    def analyze(self, ast):
        visitor = FunctionsVisitor(ast)
        visitor.visit(ast)
        return visitor.warningsList()