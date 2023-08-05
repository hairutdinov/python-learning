from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello/<name>")
def greeting(name):
    return f'Hello, {name}'

if __name__ == '__main__':
    app.run()