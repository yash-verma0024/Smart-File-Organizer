from pathlib import Path

from organizer.path_manager import create_path
from organizer.classifier import classify
from organizer.scanner import scan
from organizer.mover import move_file
from organizer.validator import is_file

def organizer_folder(folder: str | Path) -> dict:
    folder = create_path(folder)
    scan_files = scan(folder)

    # Tracking Metrics Dictionary
    stats = {
        "Files_moved" : 0,
        "Files_skipped" : 0,
        "Error_encountered" : 0
    }

    for item in scan_files:

        # Guard clause to skip non-files without throwing a full execution error
        if not is_file(item):
            stats["Files_skipped"] += 1
            continue

        try:
            # 1. Get the target destination folder from classifier
            destination_dir = folder / classify(item)

            # 2. Ensure target structure exists so move_file's is_dir check passes
            destination_dir.mkdir(
                parents=True, 
                exist_ok=True
                )

            # 3.Call your imported move utility
            move_file(source=item, destination=destination_dir)
            stats["Files_moved"] += 1

        except Exception as e:
            # Catching your custom raised error keeps the loop moving for other files
            print(f"skipping {item.name} due to -> {e}")
            stats["Error_encountered"] += 1
            continue


    return stats
        
# Testing the file

if __name__ == "__main__":
    folder = r"C:\Users\verma\Videos\New folder"
    print(organizer_folder(folder))
    print("Organization complete!")