from flask import Flask, jsonify


app = Flask(__name__) # class

@app.route('/')
def hello_work():
    return jsonify({"greeting": "Wir sind cool :-)"})