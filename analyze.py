from ast import *
import os
from rules.rule import *
from rules.eval_used import *
from rules.uncouple_method import *
from rules.dummy_if import *
from rules.uninitialized_attribute import *
from rules.suspicious_variable_name import *
from rules.never_readed_variable import *
from rules.data_class import *

path = "input-code/"
dir_list = os.listdir(path)
 
print("Analyzing files in '", path, "' :")

for file in dir_list:
    print(" ==== " + file + " ==== ")
    fileContent = open(path+file).read()
    tree = parse(fileContent)
    warnings = []
    #print('tree ->\n', dump(tree), '\n')
    for ruleClass in Rule.__subclasses__():    
        newRule = ruleClass()
        result = newRule.analyze(tree) 
        warnings.extend(result)
    for warning in warnings:
        warning.wprint()
