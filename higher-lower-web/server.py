from flask import Flask
from random import randint

app = Flask(__name__)

random_number = None

@app.route('/')
def home():
    global random_number
    random_number = randint(0, 10)
    print(random_number)
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy-downsized-large.gif" />'

@app.route('/<int:number>')
def detect_number(number):
    if number > random_number:
        return '<h1 style="color:red">Too high, try again!</h1>'
    elif number < random_number:
        return '<h1 style="color:red">Too low, try again!</h1>'
    else:
        return '<h1 style="color:green">You found me!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
