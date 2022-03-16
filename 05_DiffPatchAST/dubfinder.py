import importlib
import ast
import inspect
import sys
from textwrap import dedent
from difflib import SequenceMatcher


def find_functions(obj, path):
    '''Returns functions found in object with their path from initial place'''
    members = inspect.getmembers(obj)
    functions = []
    for elem in members:
        if inspect.isfunction(elem[1]):
            functions += [(f"{path}.{elem[0]}", elem[1]), ]  # такая схема - чтобы сохранить путь к функции
        elif inspect.isclass(elem[1]):
            if not elem[0].startswith('__'):
                functions += find_functions(elem[1], f"{path}.{elem[0]}")
    return functions

def rewrite_function(fun):
    '''Modifies function for easier similarity lookup'''
    code = dedent(inspect.getsource(fun[1]))
    tree = ast.parse(code)
    nodes = ast.walk(tree)
    for node in nodes:
        if hasattr(node, "id"):
            node.id = "_"
        elif hasattr(node, "name"):
            node.name = "_"
        elif hasattr(node, "arg"):
            node.arg = "_"
        elif hasattr(node, "attr"):
            node.attr = "_"
    return fun[0], ast.unparse(tree)        


if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Wrong count of parameters")
    sys.exit()
module_1_name = sys.argv[1]
if len(sys.argv) == 3:
    module_2_name = sys.argv[2]
module_1 = importlib.import_module(module_1_name)
functions_1 = find_functions(module_1, module_1_name)
processed_functions = []
res = []  # нужна сортировка, так бы без этого
for fun in functions_1:
    processed_functions.append(rewrite_function(fun))
if len(sys.argv) == 3:
    module_2 = importlib.import_module(module_2_name)
    functions_2 = find_functions(module_2, module_2_name)
    for fun in functions_2:
        processed_functions.append(rewrite_function(fun))
for i in range(len(processed_functions)):
    for j in range(i + 1, len(processed_functions)):
        if SequenceMatcher(None, processed_functions[i][1], processed_functions[j][1]).ratio() > 0.95:
            res.append(f"{processed_functions[i][0]} : {processed_functions[j][0]}")
res.sort()
for line in res:
    print(line)
