import os
from flask import Flask, jsonify, request, session, render_template, redirect
import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    database="flask_intro",
)

cur = connection.cursor()

# instantiating a class (Flask)
app = Flask(__name__)

## Common HTTP verbs:
# - POST
# - GET (default)
# - DELETE
# - PATCH
# - PUT


@app.route("/")
def index():
    # Fetch all the reminders from the database
    cur.execute("SELECT id, title, description FROM reminders ORDER BY id ASC")
    reminder_data = cur.fetchall()
    reminder_data = [
        {"id": item[0], "title": item[1], "description": item[2]}
        for item in reminder_data
    ]
    # reminders = jsonify({reminder_data})
    return render_template("index.html", reminders=reminder_data)


@app.route("/update", methods=["POST"])
def update_reminder():
    id = request.form.get("id")
    title = request.form.get("title")
    description = request.form.get("description")

    return render_template("update.html", id=id, title=title, description=description)


@app.route("/delete", methods=["POST"])
def delete_reminder():
    id = request.form.get("id")
    title = request.form.get("title")
    description = request.form.get("description")
    # Fetch all the reminders from the database
    cur.execute(
        f"SELECT * FROM reminders WHERE id={id} and title='{title}' and description='{description}';"
    )

    validation_check = cur.fetchone()
    print(validation_check)
    if validation_check:
        cur.execute(
            f"DELETE FROM reminders WHERE id={id} and title='{title}' and description='{description}';"
        )
        connection.commit()
    return redirect("/")


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    title = request.form.get("title")
    description = request.form.get("description")
    # Fetch all the reminders from the database
    cur.execute(
        f"INSERT INTO reminders (title, description) VALUES ('{title}', '{description}');"
    )
    connection.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5050")),
        debug=True,
    )
