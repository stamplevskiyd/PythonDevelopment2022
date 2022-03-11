import cmd
import shlex
import inspect
import readline
import pynames
from pynames import GENDER, LANGUAGE


class Name_cmd(cmd.Cmd):
    prompt = '> '

    def do_generate(self, arg):
        args = shlex.split(arg)
        if len(args) < 1 or len(args) > 3:
            print("From 1 to 3 arguments is required")
            return
        race = args[0]
        allowed_races = inspect.getmembers(pynames.generators)[1][1]  # просто нашел, что это-нужное место
        if not (race in allowed_races):
            print("Names for this race can not be generated")
            return
        gen_name, gender = '', 'male'
        if len(args) > 1:
            if args[1] == 'male' or args[1] == 'female':
                gender = args[1]
            else:
                gen_name = args[1]
            if len(args) == 3:
                gender = args[2]
        start_line = 'pynames.generators.' + race
        base = eval(start_line)
        members_list = inspect.getmembers(base)
        generator_name = [elem[0] for elem in members_list if
                          elem[0].endswith("Generator") and elem[0].startswith(gen_name)
                          and elem[0] != 'FromListGenerator'][0]  # генератор из списка, которого у нас нет
        gender_str = 'GENDER.' + gender.upper()
        start_line += '.' + generator_name + '()'
        generator_object = eval(start_line)
        print(generator_object.get_name(eval(gender_str)))



Name_cmd().cmdloop()
