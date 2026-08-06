from pathlib import Path

def create_path(path: str | Path):

    # Raise exception error on invalid inputs
    if not path:
        raise ValueError("Invalid path input")
    
    return Path(path)