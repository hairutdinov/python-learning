from flask import Flask, render_template
from random import randint
from datetime import datetime
from requests import get
from agify import Agify
from genderize import Genderize

AGIFY_ENDPOINT = 'https://api.agify.io'
GENDERIZE_ENDPOINT = 'https://api.genderize.io'

app = Flask(__name__)

@app.route('/')
def home():
    random_num = randint(1, 10)
    return render_template('index.html', num=random_num, year=datetime.today().year)

@app.route('/guess/<name>')
def guess_age_by_name(name):
    agify = Agify(name)
    genderize = Genderize(name)
    return render_template('guess.html', name=name, gender=genderize.gender, age=agify.age)

@app.route('/blog')
def get_blog():
    BLOG_ENDPOINT = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = get(BLOG_ENDPOINT)
    articles = response.json()
    return render_template('blog.html', articles=articles)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
