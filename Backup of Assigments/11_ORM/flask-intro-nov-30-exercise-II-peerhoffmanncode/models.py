from flask_sqlalchemy import SQLAlchemy
from config import db


class Reminder(db.Model):
    """ "Implement a solution using flask-sqlalchemy"""

    __tablename__ = "reminders"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return f"<Reminder id={self.id}, title='{self.title}', description='{self.description}'>"
