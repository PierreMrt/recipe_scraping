from scraper import scrap_links, scrap_recipe

from sqlite import create_connection, execute_read_query, insert_into_db

if __name__ == '__main__':
    conn = create_connection('db_recettes.sqlite')
    links = scrap_links()
    for link in links:
        recipe = scrap_recipe(link)
        insert_into_db(conn, recipe)

    read = "SELECT * FROM recipes"
    recipes = execute_read_query(conn, read)
    for recipe in recipes:
        print(recipe)

