import os
from global_functions import *


def create_project(project_name: str, creation_path: str, main_file_location: str) -> None:
    main_file_location = main_file_location.split("\\")
    main_file_location.pop(-1)
    main_file_location = "\\".join(main_file_location)

    projects_path = main_file_location + "\\commands\\create_project\\project_templates"

    if project_name == "--help" and creation_path is None:
        print("Downloaded project templates: ")
        for tem in os.listdir(projects_path):
            print(tem)
        return None

    if not os.path.exists(projects_path + "\\" + project_name):
        print("Requested project template doesn't exist. Check your spelling or install project template...")
        print("You can try 'pm.exe create-project --help' to get list of existing projects")
        return None

    clone_path(projects_path + "\\" + project_name, creation_path, False)


if __name__ == "__main__":
    pass
