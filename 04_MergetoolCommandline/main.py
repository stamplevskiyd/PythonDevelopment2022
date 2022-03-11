import cmd
import shlex
import inspect
import readline
import pynames
from pynames import GENDER, LANGUAGE


class Name_cmd(cmd.Cmd):
    prompt = '> '

    def get_args(self, arg):  # распаковка аргументов и нужные параметры примерно одинаковые
        args = shlex.split(arg)
        if len(args) < 1 or len(args) > 3:
            print("From 1 to 3 arguments is required")
            return
        race = args[0]
        allowed_races = inspect.getmembers(pynames.generators)[1][1]  # просто нашел, что это-нужное место
        if not (race in allowed_races):
            print("Names for this race can not be generated")
            return
        gen_name, info, subrace = '', '', ''  # передача и пола и language в info одновременно не имеют смысла. Пусть будет одна переменная
        if len(args) > 1:
            if args[1] == 'male' or args[1] == 'female' or args[1] == 'language':
                info = args[1]
            else:
                subrace = args[1]
            if len(args) == 3:
                info = args[2]
        start_line = 'pynames.generators.' + race
        base = eval(start_line)
        members_list = inspect.getmembers(base)
        generator_name = [elem[0] for elem in members_list if
                          elem[0].endswith("Generator") and elem[0].startswith(subrace)
                          and elem[0] != 'FromListGenerator'][0]  # генератор из списка, которого у нас нет
        start_line += '.' + generator_name + '()'
        return eval(start_line), info

    def do_generate(self, arg):
        generator_object, gender = Name_cmd.get_args(self, arg)
        if not gender:  # по умолчанию
            gender = 'male'
        gender_str = 'GENDER.' + gender.upper()
        print(generator_object.get_name(eval(gender_str)))


    def do_info(self, arg):
        generator_object, parameter = Name_cmd.get_args(self, arg)
        if parameter == 'language':
            print(*(lang for lang in generator_object.languages), sep=', ')
        else:
            if parameter:
                gender_str = 'GENDER.' + parameter.upper()
                print(generator_object.get_names_number(eval(gender_str)))
            else:
                print(generator_object.get_names_number())




Name_cmd().cmdloop()
