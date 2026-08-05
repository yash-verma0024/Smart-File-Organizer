from pathlib import Path
from organizer.path_manager import create_path
from organizer.validator import is_file
from config.settings import DEFAULT_FOLDER
from config.file_types import EXTENSION_TO_CATEGORY

"""
Classify the files on the basis of their extension
"""

def classify(path: str | Path) -> str:
    file_path = create_path(path)

    # Checking whether  the path has file or not
    if not is_file(file_path):
        raise ValueError("The provided path must refer to an existing file.")

    # Extracting File extension and store
    file_extension = file_path.suffix.lower()

    return EXTENSION_TO_CATEGORY.get(file_extension, DEFAULT_FOLDER)


if __name__ == "__main__":
    path = r"C:\Users\verma\OneDrive\Pictures\Feedback\Project\Smart-File-Organizer\organizer\classifier.py"
    print(classify(path))