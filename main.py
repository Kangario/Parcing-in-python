import requests
from bs4 import BeautifulSoup
import pandas as pd

# отправляем запрос на страницу и получаем HTML-код
url = 'https://www.marvel.com/characters'
response = requests.get(url)
html = response.text

# создаем объект BeautifulSoup для парсинга HTML-кода
soup = BeautifulSoup(html, 'html.parser')

# извлекаем список всех героев на странице
heroes = soup.find_all('a', {'class': 'explore__link'})

# создаем пустой список для хранения данных о героях
data = []

# проходимся по списку героев и извлекаем нужные данные
for hero in heroes:
    name = hero.find('p').text.strip() # извлекаем имя героя
    link = 'https://www.marvel.com' + hero['href'] # извлекаем ссылку на страницу героя
    data.append([name, link])

# создаем DataFrame из списка данных
df = pd.DataFrame(data, columns=['Name', 'Link'])

# сохраняем DataFrame в CSV-файл
df.to_csv('marvel_characters.csv', index=False)