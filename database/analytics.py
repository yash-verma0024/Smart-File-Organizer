import pandas as pd

from database.connection import get_connection

def db_to_df() -> pd.DataFrame:
    connection = get_connection()
    query = "SELECT * FROM files"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


def get_file_count_by_extension() -> pd.Series:
    df = db_to_df()
    data = df["extension"].value_counts()
    return data

def get_storage_by_extension() -> list[dict]:
    df = db_to_df()
    data = (
        df.groupby("extension")["file_size"]
        .sum()
        .div(1024 ** 3)
        .round(2)
    )
    return data

def get_largest_files() -> pd.DataFrame:
    df = db_to_df()
    data = df.nlargest(10, "file_size")
    return data


def get_database_summary() -> pd.DataFrame:
    df = db_to_df()
    data = (df.describe())
    return data

if __name__ == "__main__":
    print(get_database_summary())