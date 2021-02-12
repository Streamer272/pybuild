import sys
from commands.add_modules import *
from commands.create_project import *

args = sys.argv
args.pop(0)

try:
    command = args[0]
except:
    main_file_location = __file__.split("\\")
    main_file_location.pop(-1)
    main_file_location = "\\".join(main_file_location)
    print("No command was called. Available commands: ")
    for com in os.listdir(main_file_location + "\\commands"):
        print(com)


def main():
    if "add-modules" == command:
        try:
            args[1]
        except:
            print("One positional argument missing: path")
            return None

        add_modules(args[1])
    elif "create-project" == command:
        arg1 = None
        arg2 = None
        try:
            arg1 = args[1]

            if arg1 is None:
                raise TypeError
        except:
            print("One positional argument missing: project name")
        try:
            arg2 = args[2]

            if arg2 is None:
                raise TypeError
        except:
            if arg1 != "--help":
                print("One positional argument missing: path")

        create_project(arg1, arg2, __file__)


if __name__ == "__main__":
    main()
