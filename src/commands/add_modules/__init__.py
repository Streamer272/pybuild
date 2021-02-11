from getpass import getuser
from src.get_directory_content import *

modules_directory = "C:\\Users\\" + getuser() + "\\AppData\\Local\\Programs\\Python\\Python39\\Lib"


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


def add_modules(build_path: str) -> None:
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
    pass
