import sys

from commands.add_modules import *

args = sys.argv
args.pop(0)

build_path = args[0]


if __name__ == "__main__":
    if "add-modules" in args:
        add_modules(build_path)
