import cmd
import shlex
import pynames
import inspect
import readline


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
        generator_name, gender = None, 'male'
        if len(args) > 1:
            if args[1] == 'male' or args[1] == 'female':
                gender = args[1]
            else:
                generator_name = args[1]
            if len(args) == 3:
                gender = args[2]
        start_line = 'pynames.generators.' + race
        base = eval(start_line)
        members_list = inspect.getmembers(base)
        print(members_list)


Name_cmd().cmdloop()
