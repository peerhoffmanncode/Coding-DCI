from __future__ import annotations
from typing import Union
import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    database="postgres",
)
cur = connection.cursor()


class Reminder:
    """ORM of a Reminder database"""

    @staticmethod
    def init_database_table():
        try:
            connection = psycopg2.connect(
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432",
                database="postgres",
            )
            cur = connection.cursor()
            cur.execute("DROP TABLE IF EXISTS reminders;")
            cur.execute(
                "CREATE TABLE reminders (id SERIAL PRIMARY KEY, title VARCHAR(255), description TEXT);"
            )
            cur.execute(
                """INSERT INTO reminders (title, description)
                VALUES ('Mirjam is awesome', 'She is learning to code'),
                ('Eat', 'Food is healthy'), ('Exercise', 'Get your heart moving');"""
            )

            # persist the changes
            connection.commit()
            return "Initialized test database seccessfully ..."
        except:
            return "Something horrible happened! We might go to hell ..."

    def __init__(
        self,
        reminder_id=None,
        title: str = "",
        description: str = "",
    ) -> None:
        self.id = reminder_id
        self.title: str = title
        self.description: str = description

    def __repr__(self) -> str:
        """findes a Reminder record in the database"""
        return f"<Reminder id={self.id}, title={self.title}, description={self.description}>"

    @classmethod
    def find(cls, reminder_id: int):
        """findes a Reminder record in the database"""
        try:
            cur.execute(
                f"""SELECT id, title, description FROM reminders WHERE id={reminder_id};"""
            )
            reminder_id, title, description = cur.fetchone()  # <- tuple unpacking
            return cls(reminder_id, title, description), "Successfully saved"
        except TypeError:
            return (None, "il Reminder non é presente!")

    def save(self) -> Union[Reminder, None]:
        """
        Stores the values of title and description in the table
        """
        try:
            cur.execute(
                f"""INSERT INTO reminders (title, description)
                VALUES('{self.title}', '{self.description}') RETURNING id, title, description"""
            )
            # persist the changes
            connection.commit()
            values = cur.fetchone()
            return Reminder(
                reminder_id=values[0], title=values[1], description=values[2]
            )
        except:
            return None
