from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

DB_NAME = "flask_intro"
reminders_list = []


def db_write(query: str, mode="") -> tuple:
    """function to read data of a database"""

    # Connect to an existing database
    conn = psycopg2.connect(dbname=DB_NAME, user="postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: this creates a new table
    cur.execute(query)
    # Make the changes to the database persistent
    conn.commit()
    # read data if there is anything
    if mode == "all":
        fetched_db_result = cur.fetchone()
    else:
        fetched_db_result = cur.fetchall()
    # Close communication with the database
    cur.close()
    conn.close()
    return fetched_db_result


def db_read(query: str, type: str = "all") -> list:
    """function to write data to a database"""

    # Connect to an existing database
    conn = psycopg2.connect(dbname=DB_NAME, user="postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: this creates a new table
    if query:
        cur.execute(query)
    if type.lower() == "all":
        fetched_db_result = cur.fetchall()
    else:
        fetched_db_result = cur.fetchone()

    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()
    if fetched_db_result:
        return fetched_db_result
    else:
        return None


def convert_reminders_format(reminders: list) -> list:
    """function  to convert a list of lists/tuples, to a list of dictionaries"""

    # list comprehension approach
    if isinstance(reminders, list):
        list_of_dicts_to_return = [
            {"id": element[0], "title": element[1], "description": element[2]}
            for element in reminders
        ]
    else:
        list_of_dicts_to_return = {
            "id": reminders[0],
            "title": reminders[1],
            "description": reminders[2],
        }

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
    reminders_list = convert_reminders_format(
        db_write(
            f"INSERT INTO reminders (title, description) VALUES ('{title}','{desc}') RETURNING id, title, description;"
        )
    )
    # reminders_list = convert_reminders_format(db_read("SELECT * FROM reminders;"))
    return jsonify({"reminders": reminders_list})


@app.route("/reminders/<int:id>", methods=["GET"])
def reminder(id):
    """function to delete reminder by given id"""
    breakpoint()
    reminders_list = db_read(f"SELECT * FROM reminders WHERE id={id};", "one")
    if not reminders_list:
        return jsonify({"message": "Sorry! We can't find your reminder!"}), 404
    try:
        reminders_list = convert_reminders_format(reminders_list)
        return jsonify(reminders_list)
    except TypeError:
        return jsonify({"message": "Sorry! Something bad happen!"}), 500


@app.route("/reminders/<int:id>", methods=["DELETE"])
def delete_reminder(id):
    """function to delete a reminder entry"""

    db_write(f"DELETE FROM reminders WHERE id = {id};")
    reminders_list = convert_reminders_format(db_read("SELECT * FROM reminders;"))
    return jsonify({"reminders": reminders_list})


@app.route("/reminders/<int:id>/update", methods=["PUT"])
def update_reminder(id):
    breakpoint()
    """function to update a reminder entry"""
    try:
        reminders_list = db_write(
            f"""
                UPDATE reminders SET title = '{request.json.get("title")}',
                description = '{request.json.get("description")}' WHERE id = {id}
                RETURNING id, title, description;"""
        )
        if not reminders_list:
            return (
                jsonify({"message": "Sorry! We can't find this entry to update it!"}),
                404,
            )

        reminders_list = convert_reminders_format(reminders_list)
        return jsonify({"reminders": reminders_list})
    except:
        return jsonify({"message": "Sorry! Something bad happened!"}), 500


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
