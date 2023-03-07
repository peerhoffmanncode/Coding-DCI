from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<strong>Hello, World!</strong>"


if __name__ == "__main__":
    app.run(debug=False, port=5000)
