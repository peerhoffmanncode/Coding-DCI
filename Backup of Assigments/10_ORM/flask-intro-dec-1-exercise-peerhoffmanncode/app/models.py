from . import db
from sqlalchemy.orm import declarative_base, relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """table for users in a database"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    reminder_id = relationship("Reminder", backref="user")

    @property
    def password(self):
        raise AttributeError("password is a not readable hash value!")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "password": self.password_hash,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "reminders": [r.to_json() for r in self.reminder_id],
        }


class Reminder(db.Model):
    """table for reminder in a database"""

    __tablename__ = "reminders"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "author_id": self.user.id,
            "author": f"User [{self.user.user_name}] {self.user.first_name} {self.user.last_name} eMail: {self.user.email}",
        }
