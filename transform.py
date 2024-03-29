from ast import *
import os
from rewriter.rewriter import *
from rewriter.eval_rewriter import *
from rewriter.if_true_rewriter import *
from rewriter.plus_plus_rewrite import *
from rewriter.if_without_else_rewrite import *

path = "input-code/"
dir_list = os.listdir(path)
 
print("Transforming files in '", path, "' :")


for file in dir_list:
    print(" ==== " + file + " ==== ")
    fileContent = open(path+file).read()
    tree = parse(fileContent)
    for commandClass in RewriterCommand.__subclasses__():    
        command = commandClass()
        tree = command.apply(tree)
    # export in a new file
    f = open("transformed-code/"+file, "w")
    f.write(unparse(tree))
    f.close()
