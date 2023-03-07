from flask import Flask, jsonify
import os
from flask_cors import CORS


# see: https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# enable Cross Origin Resource Sharing
CORS(app)

app.config.from_object(os.getenv("APP_SETTINGS"))

## Functions to handle PostgreSQL connections
ENVIRONMENT = os.getenv("DOCKER_ONLY", False)


@app.route("/")
def index():
    return jsonify({"message": "hello world!"})


# TODO -> WRITE CODE TOGETHER in class
# Implement the following routes

# TODO: Part of live coding
# - /reminders (Get all reminders)
# --- add support for attribute filters
# --- /reminders/filter?name=x or ?title=xyz

# TODO: Give as exercise in class (10 to 15mins)
# - /reminders/create (Create a reminder) - (We refactor later into just one route)

# TODO: Part of live coding
# - /reminders/<id> (GET one reminder, DELETE one reminder)

# TODO: Part of live coding
# - /reminders?sort_by=asc|desc (Do some ordering)

# TODO: Part of live coding
# - /reminders/<id>/update (Edit & Update one reminder) -> UPDATE <table> SET <attribute> = <value> WHERE <an attribute> = <a value>;

# TODO: Give as exercise in class (10 to 15mins)
# - /reminders/<id>/delete (Delete a reminder)

# TODO: Part of live coding
# Other links
# SQL Aggregates concepts
# - /reminders/count?completed=false --> SELECT COUNT(*) FROM <table> where completed=true/false;
# - /reminders/count?completed=true -->

# TODO: Give as exercise in class (might take longer - all day is fine too including other tasks for the day)
# Add "name" to reminders table (Using -> ALTER), add some names to the DB
# Group reminders by who wrote the reminder
# SELECT name, COUNT(*) FROM <table> GROUP BY <name>;
# - /reminders?group_by=<attribute>


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)
