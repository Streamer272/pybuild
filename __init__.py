import os
import subprocess
import sys


args = sys.argv
args.pop(0)

build_path = args[0]
package_dir = "C:\\Users\\danko\\AppData\\Local\\Programs\\Python\\Python39\\Lib"


def get_directory_content(directory_path: str) -> list:
    ignore = [".git", ".vscode", ".vs", ".idea", ".gitignore"]

    files = os.listdir(directory_path)
    to_return = []

    for file in files:
        if file in ignore:
            next

        file_container = {}

        file_container["filename"] = file
        if (os.path.isdir(directory_path + "\\" + file)):
            file_container["type"] = "directory"
            file_container["content"] = get_directory_content(directory_path + "\\" + file)
        else:
            file_container["type"] = "file"
            file_container["content"] = open(directory_path + "\\" + file, "rb").read()
        file_container["parent"] = directory_path

        to_return.append(file_container)

    return to_return

def clone_path(old_directory_path: str, new_directory_path: str) -> None:
    old_dir_files = get_directory_content(old_directory_path)
    os.mkdir(new_directory_path)

    for file in old_dir_files:
        if file["type"] == "file":
            f = open(new_directory_path + "\\" + file["filename"], "wb")
            f.write(file["content"])
            f.close()
        else:
            clone_path(old_directory_path + "\\" + file["filename"], new_directory_path + "\\" + file["filename"])

def main() -> None:
    dir_content = get_directory_content(build_path)
    for file in dir_content:
        if file["filename"] in ("main.py", "master.py", "__init__.py"):
            content = file["content"].decode().split("\n")
            for line in content:
                if "import " in line and "from " not in line:
                    module = line.replace("import ", "")
                    clone_path(package_dir + "\\" + module, build_path)
                elif " import " in line and "from " in line:
                    module = line.replace("from ", "").split(" import ")[0]
                    clone_path(package_dir + "\\" + module, build_path)

main()
