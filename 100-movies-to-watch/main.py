import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, 'html.parser')
names = [item.getText() for item in soup.select('h3.title')]
names.reverse()

with open('movies.txt', 'w') as file:
    file.write('\n'.join(names))