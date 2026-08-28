from pathlib import Path

from config.options import CORE_OPTION, DATABASE_FOLDER, DATABASE_SEARCH, DATABASE_SORT_SEARCH
from database.file_index import *
from database.schema import create_tables
from organizer.organizer import organizer_folder
from organizer.metadata import extract_metadata
from organizer.validator import sort_data

def main():
    """
    Excecuting data pipeline
    """

    print(CORE_OPTION)
    option = int(input("Enter the option : "))

    # 1. Organize files in folder
    if option == 1:
        path = Path(input("Enter the path : "))
        data = organizer_folder(path)

        for file in data["Moved_paths"]:
            metadata = extract_metadata(file)
            insert_file(metadata)

        if data["Error_encountered"] == 0:
            print("Files saved to database")
        else:
            print("New files saved; existing files were skipped")


    # 2. Check Database
    elif option == 2:
        print(DATABASE_FOLDER)
        Database_option = int(input("Enter the option : "))

        if Database_option == 1:
            print(see_database())

        if Database_option == 2:
            print(DATABASE_SEARCH)
            search_condition = int(input("Enter the option " ))

            if search_condition == 1:
                id = int(input("Enter the id : "))
                print(search_by_id(id))

            elif search_condition not in [1,2,3]:
                return "Invalid Input"
            
            # Applying sorting query
            print(DATABASE_SORT_SEARCH)
            sort_option = int(input("Enter the option : "))

            if search_condition == 2:
                name = input("Enter the  name: ")

                if sort_option == 1:
                    print(sort_data(search_by_name(name), "file_name", descending=False))
                elif sort_option == 2:
                    print(sort_data(search_by_name(name), "file_name", descending=True))
                else:
                    return "Invalid option"

            elif search_condition == 3:
                extension = input("Enter the Extension: ")

                if sort_option == 1:
                    print(sort_data(search_by_extension(extension), "extension", descending=False))
                elif sort_option == 2:
                    print(sort_data(search_by_extension(extension), "extension", descending=True))
                else:
                    return "Invalid option"

        if Database_option == 3:
            file_id = int(input("Enter file id: "))
            new_path = Path(input("Enter the new path: "))
            update_file_path(file_id, new_path)

    else:
        return "Invalid Input"


if __name__ == "__main__":
    create_tables()
    main()