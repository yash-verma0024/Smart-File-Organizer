import hashlib
from pathlib import Path

from organizer.path_manager import create_path
from organizer.validator import is_file

def calculate_hash(path: str | Path) -> str:
    """
    Calculate SHA-256 hash for a file
    """
    path = create_path(path)

    # Validating file
    if not is_file(path):
        raise FileNotFoundError("Unable to Find the specific file.")

    # Create hash object 
    file_hash = hashlib.sha256()

    # Open the file in binary mode
    with path.open("rb") as file:
        # Read the file chunks
        while True:
            chunks = file.read(64*1024)  # Per chunks size = 64kb

            # Stop if there is no more data
            if not chunks:
                break

            # Feed the chunks into hash
            file_hash.update(chunks)

    # Return the final hexadecimal digest
    return file_hash.hexdigest()

if __name__ == "__main__":
    print(calculate_hash(r"C:\Users\verma\OneDrive\Pictures\Github\Project\Smart-File-Organizer\organizer\classifier.py"))