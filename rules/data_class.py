from . rule import *


#visita cada nodo función de un nodo ClassDef
class FunctionCounter(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.counter = 0
    
    def visit_FunctionDef(self, node: FunctionDef):
        self.counter += 1
        NodeVisitor.generic_visit(self, node)
        return self.counter


class FunctionDefVisitor(WarningNodeVisitor):
    def __init__(self, class_warning, real_total_methods, class_line, class_name):
        super().__init__()
        self.class_warning = class_warning
        self.attributes_name = dict()
        self.methods_get_names = set()
        self.methods_set_names = set()
        self.total_attributes = 0
        self.total_methods = -1
        self.real_total_methods = real_total_methods
        self.data_class = 0
        self.current_method = 0
        self.class_line = class_line
        self.class_name = class_name

    def visit_FunctionDef(self, node: FunctionDef):
        self.current_method += 1
        if node.name == '__init__':
            for node_body in node.body:
                if isinstance(node_body, Expr):
                    get_name = 'get' + node_body.value.attr.lower()
                    self.methods_get_names.add(get_name)
                    set_name = 'set' + node_body.value.attr.lower()
                    self.methods_set_names.add(set_name)
                    self.attributes_name[node_body.value.attr.lower()] = {
                        'get': get_name,
                        'set': set_name
                    }
                    self.total_attributes += 1
            self.total_methods = self.total_attributes*2
        else:
            #otros métodos
            name_lower = node.name.lower()
            if (name_lower in self.methods_get_names): 
                #body solo debe tener un return
                if(len(node.body) == 1):
                    if isinstance(node.body[0], Return) and isinstance(node.body[0].value, Attribute):
                        #preguntamos si el atributo retornado corresponde con el nombre del método
                        if self.attributes_name[node.body[0].value.attr.lower()]['get'] == name_lower:
                            self.data_class += 1 #cumplió con los establecido

            elif (name_lower in self.methods_set_names):
                if(len(node.body) == 1):
                    if isinstance(node.body[0], Assign) and isinstance(node.body[0].targets[0], Attribute):
                      #verificamos que el atributo que edita es relacionado a su nombre
                      if self.attributes_name[node.body[0].targets[0].attr.lower()]['set'] == name_lower:
                        self.data_class += 1

        if self.current_method == self.real_total_methods:
            if (self.data_class == self.total_methods) and self.data_class != 0:
                self.class_warning.addWarning('DataClass', self.class_line, 'class ' + self.class_name + ' this is a Data class!!')
        NodeVisitor.generic_visit(self, node)

#visita todos los nodos ClassDef del archivo
class ClassDefVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        
    def visit_ClassDef(self, node: ClassDef):
        #print('\t\t\nClassDef -->', dump(node), '\t\t\n')
        #print('\t\t\nClassDef -->', node.name, node.lineno, '\t\t\n')
        #visitamos nodos Assign de la clase
        ast_class= parse(node)
        visit_counter_methods = FunctionCounter()
        visit_counter_methods.visit(ast_class)
        visitor_assign = FunctionDefVisitor(self, visit_counter_methods.counter, node.lineno, node.name)
        visitor_assign.visit(ast_class)
        NodeVisitor.generic_visit(self, node)

class DataClass(Rule):
    def analyze(self, ast):
        visitor = ClassDefVisitor()
        visitor.visit(ast)
        return visitor.warningsList()