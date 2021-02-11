import os


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


if __name__ == "__main__":
    pass
