from database.connection import get_connection

def create_tables():
    """
    Creating table with all essential column
    """
    # Setting up the connection
    connection = get_connection()

    # Setting up cursor object
    cursor = connection.cursor()

    try:
        # Writing the table schema
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS files(
                id INTEGER PRIMARY KEY,
                file_name TEXT NOT NULL,
                extension TEXT NOT NULL,
                file_path TEXT NOT NULL,
                file_size INTEGER NOT NULL,
                file_hash TEXT NOT NULL,
                mime_type TEXT,
                created_at TEXT,
                modified_at TEXT
                )
        """)

        # Commit the changes
        connection.commit()

    finally:
        # Closing cursor
        cursor.close()
        # closing Connection
        connection.close()

if __name__ == "__main__":
    create_tables()
    print("Database table create successfully")