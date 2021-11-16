import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_recipes_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        duration TEXT,
        link TEXT
    );
    """
    execute_query(conn, query)

def insert_into_db(conn, name, duration, link):
    query = f"""
    INSERT INTO recipes (name, duration, link)
    VALUES
    ("\{name}\", \"{duration}\", \"{link}\");
    """
    execute_query(conn, query)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


if __name__ == '__main__':
    conn = create_connection("db_recettes.sqlite")
    create_recipes_table(conn)
    