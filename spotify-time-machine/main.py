import requests
from bs4 import BeautifulSoup

BILLBOARD_HOT_100_URL_TEMPLATE = 'https://www.billboard.com/charts/hot-100/{date}/'

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(BILLBOARD_HOT_100_URL_TEMPLATE.format(**vars()))
content = response.text

soup = BeautifulSoup(content, 'html.parser')
rows = soup.select('.o-chart-results-list-row-container'
                   ' > '
                   'ul.o-chart-results-list-row'
                   ' > '
                   'li.lrv-u-width-100p'
                   ' > '
                   'ul'
                   ' > '
                   'li.o-chart-results-list__item:first-child')

songs = []

for row in rows:
    name = row.select_one('h3.c-title').get_text().strip()
    author = row.select_one('span.c-label').get_text().strip()
    songs.append({
        'name': name,
        'author': author,
    })

with open('songs-{}'.format(date), 'w') as file:
    file.write('\n'.join(map(lambda s: '{} by {}'.format(s['name'], s['author']), songs)))
