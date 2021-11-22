import requests
from bs4 import BeautifulSoup
import re

def scrap_links(existing):
    links = []
    for page in range(1, 157):
        r = requests.get(f"https://www.regal.fr/recettes/plats?sort_by=title_1&page={page}")
        soup = BeautifulSoup(r.text, 'html.parser')
        recipes = soup.find_all('div', class_="field-item even")
        for recipe in recipes:
            try:
                link = recipe.find('a')['href']
                if check_link(link):
                    link = f"https://www.regal.fr{link}"
                    if link not in existing:
                        links.append(link)
                    else:
                        print(f'Skipping {link}, already in database')

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

    name = soup.find('h1').text
    try:
        difficulty = soup.find('div', class_='field-name-field-difficulty-level').find('a').text
    except AttributeError:
        difficulty = None
    
    try:
        cost = soup.find('div', class_='field-name-field-price-level').find('a').text
    except AttributeError:
        cost = None

    try:
        preptime = soup.find('div', class_='field-name-field-recipe-preptime').find('div', class_='field-item even').text
    except AttributeError:
        preptime = None

    try:
        cooktime = soup.find('div', class_='field-name-field-recipe-cooktime').find('div', class_='field-item even').text
    except AttributeError:
        cooktime = None

    ingredients_list = []
    try:
        ingredients = soup.find('div', class_='field-name-field-recipe-elements').find_all('div', class_='content')
        for ingredient in ingredients:
            ingredients_list.append(ingredient.text.replace('\n', ''))
    except AttributeError:
        pass

    steps_list = []
    try:
        steps = soup.find('div', class_='field-name-field-recipe-steps').find_all('p')
        for step in steps:
            steps_list.append(step.text.replace('\xa0', ''))
    except AttributeError:
        pass

    return (name, link, difficulty, cost, preptime, cooktime, '||'.join(ingredients_list), '||'.join(steps_list))


if __name__ == '__main__':
    # scrap_links()
    scrap_recipe("https://www.regal.fr/recettes/plats/poule-au-riz-7652")