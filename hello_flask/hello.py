from flask import Flask

app = Flask(__name__)

def make_bold(func):
    return lambda: '<b>{}</b>'.format(func())
def make_emphasis(func):
    return lambda: '<em>{}</em>'.format(func())
def make_underlined(func):
    return lambda: '<u>{}</u>'.format(func())


@app.route("/")
@make_bold
@make_underlined
@make_emphasis
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>")
def greeting(name):
    return f'Hello, {name}'

if __name__ == '__main__':
    app.run(debug=True)