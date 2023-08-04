import requests
from bs4 import BeautifulSoup

URL = 'https://www.ozon.ru/product/chelsi-marcelo-merotti-675093905/?avtc=1&avte=2&avts=1687244413&sh=AJiK3B4RIQ'

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, 'html.parser')
print(soup.find('span', class_='z6k'))
