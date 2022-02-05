from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/login")
def log_world():
    return "log in!!"


if __name__ == '__main__':
    app.run(debug=True)
