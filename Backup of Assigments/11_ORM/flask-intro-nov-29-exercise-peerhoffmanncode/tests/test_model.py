import unittest
import psycopg2
from models import Reminder, make_connection


# unittest example
class ReminderModel(unittest.TestCase):
    def setUp(self) -> None:
        # drop table and recreate it
        cur = make_connection("flask_test").get("cur")
        # cur.execute("DROP TABLE IF EXISTS reminders;")
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS reminders (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                description TEXT
            );"""
        )
        reminder1 = Reminder(title="eat", description="sphagetti and Broccoli")
        reminder2 = Reminder(title="buy", description="Drugs to stay awake!")
        reminder3 = Reminder(title="learn", description="crazy ORMs")

        # store a sample reminder instance for a later test
        self.reminder1 = reminder1.save()
        self.reminder2 = reminder2.save()
        self.reminder3 = reminder3.save()

    def test_save(self):
        # There is no easy way to reset the ID
        # refs: https://brianchildress.co/reset-auto-increment-in-postgres/
        # refs: https://stackoverflow.com/questions/244243/how-to-reset-postgres-primary-key-sequence-when-it-falls-out-of-sync/23390399#23390399
        self.assertEqual(
            f"<Reminder id={self.reminder1.id}, title='eat', description='sphagetti and Broccoli'>",
            str(self.reminder1),
        )

    def test_find(self):
        reminder = Reminder.find(id=self.reminder1.id)
        self.assertEqual(
            f"<Reminder id={reminder.id}, title='eat', description='sphagetti and Broccoli'>",
            str(reminder),
        )

        self.assertEqual(
            str(Reminder.find(title="a")),
            "<Reminder id=1, title='eat', description='sphagetti and Broccoli'>",
        )

    def test_find_many(self):
        """Implement different test cases where you test the exercise"""

        self.assertEqual(
            str(Reminder.find(id=2, title="buy")),
            "<Reminder id=2, title='buy', description='Drugs to stay awake!'>",
        )
        self.assertEqual(
            str(Reminder.find(title="learn", description="crazy ORMs")),
            "<Reminder id=3, title='learn', description='crazy ORMs'>",
        )
