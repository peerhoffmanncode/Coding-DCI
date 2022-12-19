# Exercise: Replace -- all manual database interactions with flask-alchemy
from flask import Flask, jsonify, request

from config import app, db
from models import Reminder

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    # Fetch all the reminders from the database
    all_reminders = Reminder.query.all()
    reminder_data = [
        {
            "id": one_reminder.id,
            "title": one_reminder.title,
            "description": one_reminder.description,
        }
        for one_reminder in all_reminders
    ]
    return jsonify({"reminders": reminder_data})


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    title = request.json.get("title", None)
    description = request.json.get("description", None)

    # create new reminder object
    new_reminder = Reminder(title=title, description=description)
    # write to db
    db.session.add(new_reminder)
    # commit changes
    db.session.commit()

    reminder_data = {
        "id": new_reminder.id,
        "title": new_reminder.title,
        "description": new_reminder.description,
    }
    return jsonify({"reminders": reminder_data})


@app.route("/reminders/<int:id>")
def reminder(id):
    reminder_data = Reminder.query.get(id)
    if not reminder_data:
        return jsonify({"message": "Reminder not found"}), 404
    try:
        reminder_dict = {
            "id": id,
            "title": reminder_data.title,
            "description": reminder_data.description,
        }
        return jsonify(reminder_dict)
    except:
        return jsonify({"message": "Sorry something bad happened"}), 500


# DELETE
@app.route("/reminders/<int:id>", methods=["DELETE"])
def delete_reminder(id):
    try:
        # find the reminder
        reminder_data = Reminder.query.get(id)
        # delete from db
        db.session.delete(reminder_data)
        # commit changes
        db.session.commit()
        return jsonify({"message": "Successfully deleted!"})
    except:
        return jsonify({"message": "Reminder not found"}), 404


@app.route("/reminders/<int:id>/update", methods=["PUT"])
def update_reminder(id):
    try:
        # find the reminder
        reminder_data = Reminder.query.get(id)
        # update the reminder
        reminder_data.title = request.json.get("title", None)
        reminder_data.description = request.json.get("description", None)
        # commit changes
        db.session.commit()
        return jsonify(
            {
                "id": reminder_data.id,
                "title": reminder_data.title,
                "description": reminder_data.description,
            }
        )
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)  # port for flask
