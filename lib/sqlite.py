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


def execute_query(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")

def create_recipes_table(conn):
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        link TEXT,
        difficulty TEXT,
        cost TEXT,
        preptime TEXT,
        cooktime TEXT,
        ingredients TEXT,
        steps TEXT
    );
    """)
    conn.commit()

def insert_into_db(conn, data):
    c = conn.cursor()
    c.execute("""
    INSERT INTO recipes (name, link, difficulty, cost, preptime, cooktime, ingredients, steps)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()

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
    