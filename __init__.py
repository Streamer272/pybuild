import os
import sys
from getpass import getuser

args = sys.argv
args.pop(0)

build_path = args[0]
modules_directory = "C:\\Users\\" + getuser() + "\\AppData\\Local\\Programs\\Python\\Python39\\Lib"


def get_directory_content(directory_path: str) -> list:
    ignore = [".git", ".vscode", ".vs", ".idea", ".gitignore"]

    files = os.listdir(directory_path)
    to_return = []

    for file in files:
        if file in ignore:
            next()

        file_container = {
            "filename": file,
            "parent": directory_path
        }

        if os.path.isdir(directory_path + "\\" + file):
            file_container["type"] = "directory"
            for file_ in get_directory_content(directory_path + "\\" + file):
                to_return.append(file_)
        else:
            file_container["type"] = "file"
            file_container["content"] = open(directory_path + "\\" + file, "rb").read()

        to_return.append(file_container)

    return to_return


def clone_path(old_directory_path: str, new_directory_path: str) -> None:
    old_dir_files = get_directory_content(old_directory_path)
    os.mkdir(new_directory_path)

    for file in old_dir_files:
        if file["type"] == "file":
            new_dir_path = new_directory_path + "\\" + file["parent"].replace(old_directory_path, "")
            if not os.path.exists(new_dir_path):
                os.mkdir(new_dir_path)

            f = open(new_dir_path + "\\" + file["filename"], "wb")
            f.write(file["content"])
            f.close()


def add_modules() -> None:
    dir_content = get_directory_content(build_path)

    for file in dir_content:
        if ".py" in file["filename"] and "file" == file["type"]:
            for line in file["content"].decode().replace("\r", "").split("\n"):
                if "import" in line:
                    module = ""

                    if "import" in line and "from" not in line:
                        module = line.replace("import ", "")
                    elif "import" in line and "from" in line:
                        module = line.replace("from ", "").split(" import ")[0]

                    for file_ in dir_content:
                        if module in file_["filename"]:
                            next

                    if not os.path.exists(build_path + "\\" + module):
                        print("Cloning module " + module + "...")
                        clone_path(modules_directory + "\\" + module, build_path + "\\" + module)
                        print("Module " + module + " cloned")
                    else:
                        print("Couldn't clone module " + module + " because targeted directory already exists")


if __name__ == "__main__":
    if "--clone-modules" in args:
        add_modules()
