from organizer.path_manager import create_path
from organizer.validator import is_file
from pathlib import Path
from datetime import datetime
from organizer.hasher import calculate_hash

def extract_metadata(path: str | Path) -> dict:
    """
    Extract metadata from a file.

    """
    path = create_path(path)

    # raising error if file not exist
    if not is_file(path):
        raise FileNotFoundError(f"{path.name} is not a valid file")

    file_stat = path.stat()

    metadata = {
        "name" : path.name,
        "stem" : path.stem,
        "extension" : path.suffix.lower(),
        "parent" : str(path.parent),
        "path" : str(path.resolve()),
        "size" : file_stat.st_size,
        "hash" : calculate_hash(path),
        "created_at": datetime.fromtimestamp(file_stat.st_ctime).isoformat(sep=" ", timespec="seconds"),
        "modified_at": datetime.fromtimestamp(file_stat.st_mtime).isoformat(sep=" ", timespec="seconds"),
    }

    return metadata

# Temporary testing
if __name__ == "__main__":
    path = r"C:\Users\verma\OneDrive\Pictures\Github\Project\Smart-File-Organizer\organizer\metadata.py"
    print(extract_metadata(path))