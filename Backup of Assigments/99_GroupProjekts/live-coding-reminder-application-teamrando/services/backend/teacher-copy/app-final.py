from flask import Flask, jsonify, request

# Debugging through docker
# from remote_pdb import RemotePdb
# RemotePdb("0.0.0.0", 4444).set_trace()

# import redis
import psycopg2
import os
from flask_cors import CORS


# see: https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# enable Cross Origin Resource Sharing
CORS(app)

# TODO: Store configuration in a class
# app.config.from_object(os.getenv("APP_SETTINGS"))

# REDIS_HOST = os.getenv('REDIS_HOST')
# print("@@@@", REDIS_HOST)

# # Connecting to redis
# r = redis.Redis(host='redis', port=6379, db=0)
# r.set('foo', 'bar')

## Functions to handle PostgreSQL connections
ENVIRONMENT = os.getenv("DOCKER_ONLY", False)


def connect_to_db():
    # TODO: Show students without the function, then refactor

    # This is being done because some students did not study Docker
    host = "postgres" if ENVIRONMENT else "localhost"

    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host=host,
        port="5432",
        database="flask_project",
    )
    cur = connection.cursor()
    return connection, cur


# Initial Setup
# create tables for reminders
def initial_setup():
    connection, cur = connect_to_db()
    cur.execute(
        """
            CREATE TABLE IF NOT EXISTS reminders(
                id SERIAL PRIMARY KEY, 
                title VARCHAR(255),
                description TEXT, 
                completed BOOL DEFAULT false)
                """
    )
    connection.commit()
    connection.close()


initial_setup()


@app.route("/")
def index():
    return jsonify({"message": "hello world!"})


@app.route("/reminders")
def reminders():
    connection, cur = connect_to_db()

    # Get all reminders from the database
    cur.execute("SELECT * FROM reminders")

    # Store the values of the reminders
    reminders = cur.fetchall()

    # close the connection to the db
    connection.close()
    columns = ["id", "title", "description", "completed"]
    json_response = []
    for value in reminders:
        json_response.append(dict(zip(columns, value)))
    return jsonify(json_response), 200


# TODO: Exercise (Create a new route called, /reminders/exercise-1 and Return only id and title in the JSON output)


@app.route("/reminders/create", methods=["POST"])
def create_reminders():
    # TODO: What other data can be collected if you want a reminder
    """
    Create a reminder
    Send payload that looks like this:

    {
        "title": "<some title>",
        "description": "<some description>",
    }
    """
    connection, cur = connect_to_db()

    # TODO: What happens if an error occurs, what should we do?
    title = request.json.get("title", None)
    description = request.json.get("description")

    # Get all reminders from the database
    cur.execute(
        f"INSERT INTO reminders (title, description) values('{title}', '{description}')"
    )
    connection.commit()
    connection.close()
    return jsonify({"message": "Successfully saved"}), 201


@app.route("/reminders/<int:id>", methods=["DELETE"])
def delete_reminder(id):
    # TODO: Method not Implemented
    print("@@@@ DELETED", id)
    return jsonify(None), 200


@app.route("/reminders/<int:id>")
def find_one_reminder(id):
    """
    This route retrieves a single reminder
    """
    connection, cur = connect_to_db()

    # Get all reminders from the database
    cur.execute(f"SELECT * FROM reminders WHERE id={id}")
    reminder = cur.fetchone()
    connection.close()

    # TODO: Exercise - return a dictionary-like object that looks like this:
    # {
    #     "completed": false,
    #     "description": "description",
    #     "id": 1,
    #     "title": "title"
    # }

    return jsonify(reminder)


# TODO: Left with
# - /reminders/<id>/update (Edit & Update one reminder)
# - /reminders/<id>/delete (Delete a reminder)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)
