from . rule import *


class AttributeUsageVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()

    #Caso 1: clase Assign pertenece a nodos asignados (no self)
    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], Name):
            name = node.targets[0].id
            if name.__len__() == 1:
                self.addWarning('SuspiciousVariableName', node.lineno, 'attribute '+ node.targets[0].id + '  has a single-letter name')
        NodeVisitor.generic_visit(self, node)

    #Caso 2 clase Attribute pertenece a nodos asignados como: self.attribute
    def visit_Attribute(self, node: Attribute):
        if len(node.attr) == 1:
            self.addWarning('SuspiciousVariableName', node.lineno, 'attribute '+ node.attr + ' has a single-letter name')
        NodeVisitor.generic_visit(self, node)

    


class SuspiciousVariableNameRule(Rule):
    def analyze(self, ast):
        visitor = AttributeUsageVisitor()
        visitor.visit(ast)
        return visitor.warningsList()