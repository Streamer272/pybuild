import os
import subprocess


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


def clone_path(old_directory_path: str, new_directory_path: str, create_new_dir: bool) -> None:
    old_dir_files = get_directory_content(old_directory_path)
    if create_new_dir:
        os.mkdir(new_directory_path)

    for file in old_dir_files:
        if file["type"] == "file":
            new_dir_path = new_directory_path + "\\" + file["parent"].replace(old_directory_path, "")
            if not os.path.exists(new_dir_path):
                os.mkdir(new_dir_path)

            f = open(new_dir_path + "\\" + file["filename"], "wb")
            f.write(file["content"])
            f.close()


def is_pip_installed():
    try:
        out = subprocess.check_output("pip --version")
    except FileNotFoundError:
        return False
    return "is not recognized" not in out.decode()


if __name__ == "__main__":
    pass
