# Exercise: Replace -- all manual database interactions with our ORM
from flask import Flask, jsonify, request
from models import Reminder

app = Flask(__name__)


@app.route("/")
def index():
    # Fetch all the reminders from the database
    all_reminders = Reminder.all()
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

    new_reminder = Reminder(title=title, description=description).save()
    reminder_data = {
        "id": new_reminder.id,
        "title": new_reminder.title,
        "description": new_reminder.description,
    }
    return jsonify({"reminders": reminder_data})


@app.route("/reminders/<int:id>")
def reminder(id):
    reminder_data = Reminder.find(id)
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
    Reminder.delete(id)
    return jsonify({"message": "Successfully deleted!"})


@app.route("/reminders/<int:id>/update", methods=["PUT"])
def update_reminder(id):
    the_reminder = Reminder.find(id)
    the_reminder.update(
        title=request.json.get("title", None),
        description=request.json.get("description", None),
    )
    try:
        return jsonify(
            {
                "id": the_reminder.id,
                "title": the_reminder.title,
                "description": the_reminder.description,
            }
        )
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)  # port for flask
