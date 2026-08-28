
from database.connection import get_connection

def delete_values():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            DROP TABLE files
        """)

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
    delete_values()