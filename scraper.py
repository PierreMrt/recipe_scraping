import requests
from bs4 import BeautifulSoup
import re

from sqlite import insert_into_db

def scrap_links():
    links = []
    for page in range(1, 11):
        r = requests.get(f"https://www.regal.fr/recettes/plats?sort_by=title_1&page={page}")
        soup = BeautifulSoup(r.text, 'html.parser')
        recipes = soup.find_all('div', class_="field-item even")
        for recipe in recipes:
            try:
                link = recipe.find('a')['href']
                if check_link(link):
                    links.append(f"https://www.regal.fr{link}")
            except TypeError:
                # Not a recipe link
                pass
    return links

def check_link(link):
    if re.search('/recettes/.+', link):
        return True
    else:
        return False


def scrap_recipe(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')

    try:
        name = soup.find('h1').text
        difficulty = soup.find('div', class_='field-name-field-difficulty-level').find('a').text
        cost = soup.find('div', class_='field-name-field-price-level').find('a').text
        preptime = soup.find('div', class_='field-name-field-recipe-preptime').find('div', class_='field-item even').text
        cooktime = soup.find('div', class_='field-name-field-recipe-cooktime').find('div', class_='field-item even').text

        ingredients_list = []
        ingredients = soup.find('div', class_='field-name-field-recipe-elements').find_all('div', class_='content')
        for ingredient in ingredients:
            ingredients_list.append(ingredient.text.replace('\n', ''))

        steps_list = []
        steps = soup.find('div', class_='field-name-field-recipe-steps').find_all('p')
        for step in steps:
            steps_list.append(step.text.replace('\xa0', ''))

        return [name, link, difficulty, cost, preptime, cooktime, ingredients_list, steps_list]
    except AttributeError as e:
        print(f'An error occured: {e}\n Unable to scrap: {link}')
        return None

    
  


if __name__ == '__main__':
    # scrap_links()
    scrap_recipe("https://www.regal.fr/recettes/plats/poule-au-riz-7652")