from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

DB_NAME = "flask_intro"
reminders_list = []


def db_write(query: str) -> None:
    """function to read data of a database"""

    # Connect to an existing database
    conn = psycopg2.connect(dbname=DB_NAME, user="postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: this creates a new table
    cur.execute(query)
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()


def db_read(query: str) -> list:
    """function to write data to a database"""

    # Connect to an existing database
    conn = psycopg2.connect(dbname=DB_NAME, user="postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: this creates a new table
    if query:
        cur.execute(query)
    fetched_db_result = cur.fetchall()
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()
    return fetched_db_result


def convert_reminders_format(reminders: list) -> list:
    """function  to convert a list of lists, to a list of dictionaries"""

    # list comprehension approach
    list_of_dicts_to_return = [
        {"title": element[0], "description": element[1]} for element in reminders
    ]
    return list_of_dicts_to_return


@app.route("/", methods=["GET"])
def index():
    """function to implement the logic of the index site"""

    reminders_list = convert_reminders_format(db_read("SELECT * FROM reminders;"))
    return jsonify({"reminders": reminders_list})


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    """function to implement the logic to add reminders"""

    title = request.json.get("title")
    desc = request.json.get("description")
    db_write(f"INSERT INTO reminders (title, description) VALUES ('{title}','{desc}');")
    reminders_list = convert_reminders_format(db_read("SELECT * FROM reminders;"))
    return jsonify({"reminders": reminders_list})


@app.route("/wipe", methods=["GET"])
def wipeout_db():
    """function to wipe out and reinit the database"""

    db_write(f"DROP TABLE IF EXISTS reminders;")
    db_write(
        f"CREATE TABLE IF NOT EXISTS reminders (title VARCHAR(255) NOT NULL, description TEXT);"
    )
    reminders_list = convert_reminders_format(db_read("SELECT * FROM reminders;"))
    return jsonify({"reminders": reminders_list})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
