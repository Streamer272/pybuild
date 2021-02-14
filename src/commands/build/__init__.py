import os
from global_functions import *
from commands.add_modules import *


def replace_import(file_path: str, filename: str) -> None:
    file = open(filename, "r")
    file_content = file.read().split("\n")
    add_modules("auto", file_path)

    for line in file_content:
        line = line.replace("\r", "")
        if "import" in line:
            if "from" not in line:
                module = line.replace("import ")
            else:
                module = line.replace("from", "").split(" import ")[0]

            path_content = os.listdir(file_path)
            if module in path_content:
                if os.path.isfile(file_path + "\\" + module):
                    file_ = open(file_path + "\\" + module, "r")
                    file_content.insert(0, file_.read())
                    file_.close()
                else:
                    file_ = open(file_path + "\\" + module + "\\__init__.py", "r")
                    file_content.insert(0, file_.read())
                    file_.close()

    file.close()


def build(build_path: str) -> None:
    os.mkdir(build_path + "\\build")
    main_file = open(build_path + "\\build\\main.py", "w")

    if os.path.exists(build_path + "\\__init__.py"):
        main_file.write(open(build_path + "\\__init__.py", "r").read())
    elif os.path.exists(build_path + "\\main.py"):
        main_file.write(open(build_path + "\\main.py", "r").read())
    elif os.path.exists(build_path + "\\master.py"):
        main_file.write(open(build_path + "\\master.py", "r").read())

    while "import" in open(build_path + "\\build\\main.py", "r").read():
        replace_import(build_path, build_path + "\\build\\main.py")

    main_file.close()


if __name__ == "__main__":
    pass
