import importlib
import ast
import inspect
import sys
from textwrap import dedent


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


if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Wrong count of parameters")
    sys.exit()
module_1_name = sys.argv[1]
if len(sys.argv) == 3:
    module_2_name = sys.argv[2]
module_1 = importlib.import_module(module_1_name)
functions = find_functions(module_1, module_1_name)
for fun in functions:
    code = dedent(inspect.getsource(fun[1]))
    tree = ast.parse(code)
    nodes = ast.walk(tree)
    #new_nodes = []
    for node in nodes:
        if hasattr(node, "id"):
            node.id = "_"
        elif hasattr(node, "name"):
            node.name = "_"
        elif hasattr(node, "arg"):
            node.arg = "_"
        elif hasattr(node, "attr"):
            node.attr = "_"
    print(ast.unparse(tree))

