import shutil
from pathlib import Path
from organizer.path_manager import create_path
from organizer.validator import is_file, is_dir

def move_file(source: str | Path, destination: str | Path) -> Path:
    source = create_path(source)
    destination = create_path(destination)

    # Checking does source really a file
    if not is_file(source):
        raise ValueError(f"file : {source} not found")

    # Checking destination exist
    if not is_dir(destination):
        raise NotADirectoryError("Destination not found")

    # Duplicate Check
    target_file_path = destination / source.name
    if target_file_path.exists():
        raise FileExistsError("File already exist.")

    # Moving file
    shutil.move(source,target_file_path)

    return target_file_path

if __name__ == "__main__":
    print(move_file(r"C:\Users\verma\OneDrive\Pictures\Feedback\Project\Smart-File-Organizer\organizer\mover.py",r"C:\Users\verma\OneDrive\Pictures\Feedback\Project\Smart-File-Organizer\logs"))