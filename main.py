from scraper import scrap

from sqlite import create_connection, execute_read_query

if __name__ == '__main__':
    conn = create_connection('db_recettes.sqlite')
    scrap(conn)

    read = "SELECT * FROM recipes"
    recipes = execute_read_query(conn, read)
    for recipe in recipes:
        print(recipe)

