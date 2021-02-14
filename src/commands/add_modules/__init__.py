import os
from getpass import getuser
from global_functions import *

modules_directory = "C:\\Users\\" + getuser() + "\\AppData\\Local\\Programs\\Python\\Python39\\Lib"


def is_module(module_name: str) -> bool:
    return os.path.exists(modules_directory + "\\" + module_name)


def add_modules(module: str, build_path: str) -> None:
    if not os.path.exists(modules_directory + "\\" + module):
        print("Module is not found. Downloading module...")
        if not is_pip_installed():
            print("Couldn't find pip, download terminated. Please install pip...")
            return None
        os.system("pip install " + module)
        print("Module installed successfully...")

    if module != "auto":
        dir_content = get_directory_content(build_path)

        for file in dir_content:
            if ".py" == file["filename"][-3:-1] + file["filename"][-1] and "file" == file["type"]:
                file_content = file["content"].decode().replace("\r", "").split("\n")
                for line in file_content:
                    if "import" in line:
                        module = ""
                        execute_command = True

                        if "import" in line and "from" not in line:
                            module = line.replace("import ", "")
                        elif "import" in line and "from" in line:
                            module = line.replace("from ", "").split(" import ")[0]

                        for file_ in dir_content:
                            if is_module(file_["parent"].replace(build_path, "")) and file_["parent"].replace(build_path, "") != "":
                                execute_command = False

                        if not os.path.exists(build_path + "\\" + module) and execute_command:
                            try:
                                print("Cloning module " + module + "...")
                                clone_path(modules_directory + "\\" + module, build_path + "\\" + module, True)
                                print("Module " + module + " cloned successfully...")

                            except:
                                print("An error occurred when executing command...")

                        elif not execute_command:
                            print("Couldn't add module " + module + " because module is already added...")

                        else:
                            print("Couldn't add module " + module + " because targeted directory already exists...")

    else:
        clone_path(modules_directory + "\\" + module, build_path + "\\" + module, True)


if __name__ == "__main__":
    pass
