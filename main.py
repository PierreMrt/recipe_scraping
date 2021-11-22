from scraper import scrap_links, scrap_recipe

from sqlite import create_connection, execute_read_query, insert_into_db

def main():
    conn = create_connection('db_recettes.sqlite')

    existing = execute_read_query(conn, "SELECT link FROM recipes")
    existing = [item for t in existing for item in t] # Transforming list of tuples into list
    print(len(existing))

    # links = scrap_links(existing)
    
    # for link in links:
    #     recipe = scrap_recipe(link)
    #     insert_into_db(conn, recipe)

    # recipes = execute_read_query(conn, "SELECT * FROM recipes")
    # for recipe in recipes:
    #     print(len(recipe))

if __name__ == '__main__':
    main()
