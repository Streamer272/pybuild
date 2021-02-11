import sys

from commands.add_modules import *

args = sys.argv
args.pop(0)

command = args[0]
path = args[1]


if __name__ == "__main__":
    if "add-modules" == command:
        add_modules(path)
