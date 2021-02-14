import os
import subprocess
from global_functions import *
from commands.add_modules import *


def replace_import(file_path: str, filename: str) -> None:
    file = open(file_path + "\\" + filename, "r")
    file_content = file.read().replace("\r", "").split("\n")
    add_modules("auto", file_path)

    for line in file_content:
        if "import" in line:
            module = ""
            if "from" not in line:
                module = line.replace("import ")
            else:
                module = line.replace("from", "").split(" import ")[0]

    file.close()


def build(build_path: str) -> None:
    os.mkdir(build_path + "\\build")
    main_file = open(build_path + "\\build\\main.py", "w")

    main_file.close()


if __name__ == "__main__":
    pass
