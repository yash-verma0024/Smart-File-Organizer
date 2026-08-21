from database.connection import get_connection

def see_database():
    """
    See All records from the database
    """
    # Establish database connection
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # view all record
        cursor.execute("""
            SELECT * FROM files
        """)
        connection.commit()
    finally:
        cursor.close()
        connection.close()


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
                file_hash,
                mime_type,
                created_at,
                modified_at
            )
            VALUES (?,?,?,?,?,?,?,?)
        """, (
            metadata["stem"],
            metadata["extension"],
            metadata["path"],
            metadata["size"],
            metadata["hash"],
            None,
            metadata["created_at"],
            metadata["modified_at"]
        ))
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def search_by_extension(extension: str) -> list[dict]:
    """
    Return all indexed files matching the given extension
    """
    extension = extension.lower()

    # establishing connections
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT id, 
                file_name,
                extension,
                file_path,
                file_size,
                file_hash,
                mime_type,
                created_at,
                modified_at
            FROM files
            WHERE extension = ?
    """, (extension,))
        
        rows = cursor.fetchall()
        results = []

        for row in rows:
            results.append({
                "id" : row[0],
                "file_name" : row[1],
                "extension" : row[2],
                "file_path" : row[3],
                "file_size" : row[4],
                "file_hash" : row[5],
                "mime_type" : row[6],
                "created_at" : row[7],
                "modified_at" : row[8]
            })

        return results
    finally:
        cursor.close()
        connection.close()


def search_by_name(file_name: str) -> list[dict]:
    """
    Return all indexed files matching the given file name.
    """
    # Setting up connections
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT id,
                file_name,
                extension,
                file_path,
                file_size,
                file_hash,
                mime_type,
                created_at,
                modified_at
            FROM files
            WHERE file_name = ?
        """, (file_name,))

        rows = cursor.fetchall()
        results = []
        for name in rows:
            results.append({
                "id" : name[0],
                "file_name" : name[1],
                "extension" : name[2],
                "file_path" : name[3],
                "file_size" : name[4],
                "file_hash" : name[5],
                "mime_type" : name[6],
                "created_at" : name[7],
                "modified_at" : name[8]
            })

        return results
    finally:
        cursor.close()
        connection.close()


def update_file_path(file_id: int, new_path: str) -> None:
    """
    Update the stored path of an indexed file
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            UPDATE files
            SET file_path = ?
            WHERE id = ?
        """, 
        (new_path, file_id, ))

        connection.commit()
    finally:
        cursor.close()
        connection.close()


def search_by_path(file_path: str) -> list[dict]:
    """
    Return all indexes files matching the given file path
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT id,
                file_name,
                extension,
                file_path,
                file_size,
                file_hash,
                mime_type,
                created_at,
                modified_at
            FROM files
            WHERE file_path = ?
        """,
        (file_path,))

        rows = cursor.fetchall()
        results = []

        for row in rows:
            results.append({
                "id" : row[0],
                "file_name" : row[1],
                "extension" : row[2],
                "file_path" : row[3],
                "file_size" : row[4],
                "file_hash" : row[5],
                "mime_type" : row[6],
                "created_at" : row[7],
                "modified_at" : row[8]
            })

        return results
    finally:
        cursor.close()
        connection.close()


def search_by_hash(file_hash: str) -> list[dict]:
    """
    Return all indexes files matching the given file hash
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT id,
                file_name,
                extension,
                file_path,
                file_size,
                file_hash,
                mime_type,
                created_at,
                modified_at
            FROM files
            WHERE file_hash = ?
        """,
        (file_hash,))

        rows = cursor.fetchall()
        results = []
        for row in rows:
            results.append({
                "id" : row[0],
                "file_name" : row[1],
                "extension" : row[2],
                "file_path" : row[3],
                "file_size" : row[4],
                "file_hash" : row[5],
                "mime_type" : row[6],
                "created_at" : row[7],
                "modified_at" : row[8]
            })

        return results
    finally:
        cursor.close()
        connection.close()


def search_by_condiation(column_name: str, condition: str) -> list[dict]:
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT id,
                file_name,
                extension,
                file_path,
                file_size,
                file_hash,
                mime_type,
                created_at,
                modified_at
            FROM files
            ORDER BY ? ?
        """,
        (column_name, condition))

        rows = cursor.fetchall()
        results = []
        for row in rows:
            results.append({
                "id" : row[0],
                "file_name" : row[1],
                "extension" : row[2],
                "file_path" : row[3],
                "file_size" : row[4],
                "file_hash" : row[5],
                "mime_type" : row[6],
                "created_at" : row[7],
                "modified_at" : row[8]
            })

        return results
    finally:
        cursor.close()
        connection.close()


def sync_hash(metadata: dict) -> None:
    """
    Synchronize the database records using the file hash
    """
    existing_files = search_by_hash(metadata["hash"])

    # File with this hash does not exist in database
    if not existing_files:
        insert_file(metadata)
        return

    # Existing Records
    existing_file = existing_files[0]

    # Same file content but different location
    if existing_file["file_path"] != metadata["path"]:
        update_file_path(
            existing_file["id"],
            metadata["path"]
        )
