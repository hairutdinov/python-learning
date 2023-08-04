from bs4 import BeautifulSoup
import requests

# with open('website.html') as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.ul)
# print(soup.find_all(name='a'))
# print([tag.getText() for tag in soup.find_all(name='a')])
# print([tag.get('href') for tag in soup.find_all(name='a')])
# print(soup.find(name='h1', id='name'))

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

# print(soup.select_one('p a'))


response = requests.get('https://news.ycombinator.com/news')
content = response.text

soup = BeautifulSoup(content, "html.parser")

articles = soup.select('span.titleline > a')
scores = soup.select('span.score')

article_texts = [link.getText() for link in articles]
article_links = [link.get('href') for link in articles]
article_upvotes = [int(score.getText().split()[0]) for score in scores]

max_votes = max(article_upvotes)
max_votes_article_index = article_upvotes.index(max_votes)

print(article_texts[max_votes_article_index])
print(article_links[max_votes_article_index])
