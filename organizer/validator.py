from pathlib import Path
from operator import itemgetter

from organizer.path_manager import create_path

"""
Scan the file and validate it weather it is file folder readable or what
"""

def file_exist(path: str | Path) -> bool:
    path = create_path(path)
    return path.exists()

def is_file(path: str | Path) -> bool:
    path = create_path(path)
    return path.is_file()

def is_dir(path: str | Path) -> bool:
    path = create_path(path)
    return path.is_dir()

def is_readable(path: str | Path) -> bool:
    path = create_path(path)

    if not path.exists():
        return False

    try:
        with path.open("r"):
            return True
    except (PermissionError, IsADirectoryError, FileNotFoundError):
        return False
    

def is_writable(path: str | Path) -> bool:
    path = create_path(path)

    if not path.exists():
        return False

    try:
        with path.open("a"):
            return True
    except (PermissionError, IsADirectoryError, FileNotFoundError):
        return False


# Function for sorting the value of metadata 
def sort_data(data, sort_column, descending=False):
    return sorted(data, key=itemgetter(sort_column), reverse=descending)


# Just for Checking code runs fine or not

def main(path):
    return {
        "is_exist" : file_exist(path),
        "is_file" : is_file(path),
        "is_dir" : is_dir(path),
        "is_readable" : is_readable(path),
        "is_writable" : is_writable(path)
    }

path = create_path("Smart-File-Organizer\organizer\path_manager.py")
if __name__ == "__main__":
    print(main(path))