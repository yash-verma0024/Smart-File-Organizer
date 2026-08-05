from pathlib import Path
from organizer.path_manager import create_path
from organizer.validator import is_dir

def scan(path: str | Path) -> list[Path]:
    """
    Scan a directory and return all files in it (non-recursive).
    """
    path = create_path(path)

    if not is_dir(path):
        raise NotADirectoryError(f"'{path}' is not a valid directory.")
    return [item for item in path.iterdir() if item.is_file()]


# Testing 

# Temporary testing only
if __name__ == "__main__":
    test_path = Path("organizer")
    print(scan(test_path))
