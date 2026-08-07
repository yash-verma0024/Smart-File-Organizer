from database.connection import get_connection

def insert_file(metadata: dict) -> None:
    """
    Insert one file's metadata as a record in the files table.
    """

    # Establish database connection
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Inserting values
        cursor.execute("""
            INSERT INTO files (
                file_name,
                extension,
                file_path,
                file_size,
                mime_type,
                created_at,
                modified_at
            )
            VALUES (?,?,?,?,?,?,?)
        """, (
            metadata["stem"],
            metadata["extension"],
            metadata["path"],
            metadata["size"],
            None,
            metadata["created_at"],
            metadata["modified_at"]
        ))
        connection.commit()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    from organizer.metadata import extract_metadata
    insert_file(extract_metadata(r"C:\Users\verma\OneDrive\Pictures\Github\Project\Smart-File-Organizer\organizer\classifier.py"))
    print("Done")