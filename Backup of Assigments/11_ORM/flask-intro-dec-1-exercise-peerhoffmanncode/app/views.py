from flask import jsonify, request
from . import create_app, db
from .models import Reminder, User

app = create_app()

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    reminder_data = [item.to_json() for item in Reminder.query.all()]
    return jsonify({"reminders": reminder_data})


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    try:
        user_id = request.json.get("user", None)
        if user_id:
            title = request.json.get("title", None)
            description = request.json.get("description", None)
            added_reminder = Reminder(
                title=title, description=description, user_id=user_id
            )
            db.session.add(added_reminder)
            db.session.commit()
            return jsonify({"reminder": added_reminder.to_json()})
        else:
            return jsonify({"message": "Missing username for this reminder!"}), 500
    except Exception as e:
        return jsonify({"message": f"Something bad happened: {e}"}), 500


@app.route("/reminders/<int:reminder_id>")
def reminder(reminder_id):
    try:
        reminder_data = Reminder.query.get(reminder_id)
        if not reminder_data:
            return jsonify({"message": "Reminder not found"}), 404
        return jsonify({"reminder": reminder_data.to_json()})
    except Exception as e:
        return jsonify({"message": f"Something bad happened: {e}"}), 500


@app.route("/reminders/<int:reminder_id>", methods=["DELETE"])
def delete_reminder(reminder_id):
    try:
        reminder_data = Reminder.query.get(reminder_id)
        db.session.delete(reminder_data)
        db.session.commit()
        return jsonify({"message": "Successfully deleted!"})
    except Exception as e:
        return jsonify({"message": f"Something bad happened: {e}"}), 500


@app.route("/reminders/<int:reminder_id>/update", methods=["PUT"])
def update_reminder(reminder_id):
    try:
        reminder_data = Reminder.query.get(reminder_id)
        reminder_data.user_id = request.json.get("user", reminder_data.user_id)
        reminder_data.title = request.json.get("title", reminder_data.title)
        reminder_data.description = request.json.get(
            "description", reminder_data.description
        )
        db.session.commit()
        return jsonify({"reminder": reminder_data.to_json()}), 201
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404


@app.route("/users-list")
def users_list():
    users_data = [item.to_json() for item in User.query.all()]
    return jsonify({"users": users_data})


@app.route("/user-add", methods=["POST"])
def create_user():
    try:
        user_name = request.json.get("username", None)
        password = request.json.get("password", None)
        first_name = request.json.get("firstname", None)
        last_name = request.json.get("lastname", None)
        email = request.json.get("email", None)

        new_user = User(
            user_name=user_name,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_json()), 201
    except TypeError:
        return jsonify({"message": "User not found"}), 404


@app.route("/<int:user_id>/user-update", methods=["PUT"])
def update_user(user_id):
    try:
        user_data = User.query.get(user_id)

        user_data.user_name = request.json.get("username", user_data.user_name)
        password = request.json.get("password", None)
        if password:
            user_data.password = password
        user_data.first_name = request.json.get("firstname", user_data.first_name)
        user_data.last_name = request.json.get("lastname", user_data.last_name)
        user_data.email = request.json.get("email", user_data.email)
        db.session.commit()
        return jsonify(user_data.to_json()), 201
    except TypeError:
        return jsonify({"message": "User not found"}), 404


@app.route("/<int:user_id>/user-delete", methods=["DELETE"])
def delete_user(user_id):
    try:
        user_data = User.query.get(user_id)
        db.session.delete(user_data)
        db.session.commit()
        return jsonify({"message": "User deleted!"})
    except TypeError:
        return jsonify({"message": "User not found"}), 404


@app.route("/user/<int:user_id>", methods=["GET"])
def show_user(user_id):
    try:
        user_data = User.query.get(user_id)
        return jsonify({"user": user_data.to_json()})
    except:
        return jsonify({"message": "User not found"}), 404
