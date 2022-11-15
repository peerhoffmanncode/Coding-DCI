from flask import Flask, jsonify, request


app = Flask(__name__)

# methods that represents URLs or links

# Home root route
REMINDERS = []


@app.route("/", methods=["GET"])
def index():
    return jsonify({"name": "your_first_name"})


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    REMINDERS.append(request.json)
    return jsonify({"reminders": REMINDERS})


# Core http verbs
# - get
# - post
# - delete
# - patch


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
