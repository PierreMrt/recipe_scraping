import requests
from bs4 import BeautifulSoup

from sqlite import insert_into_db

def scrap(conn):
    r = requests.get("https://www.marmiton.org/recettes/top-internautes-plat-principal.aspx")
    soup = BeautifulSoup(r.text, 'html.parser')
    recipe_cards = soup.find_all('div', class_='recipe-card')
    for recipe in recipe_cards:
        link = recipe.find('a')['href']
        duration = recipe.find('span', class_="recipe-card__duration__value").text
        name = recipe.find('h4').text
        insert_into_db(conn, name, duration, link)
    


if __name__ == '__main__':
    recipes = scrap()
    # for recipe in recipes:
    #     print(f"{recipe}: {recipes[recipe]}")