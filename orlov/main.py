import requests
from bs4 import BeautifulSoup

URL = 'https://bileton.ru/events/sergey-orlov-ustanovka-byt-99017#places'

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, 'html.parser')
free = soup.select('div.venue__free > strong:nth-child(1)')[0].text
print(free)