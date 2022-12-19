import unittest
from models import Reminder


## init database for testing
print(Reminder.init_database_table())


class Test(unittest.TestCase):
    """testing the Reminder class and its methods"""

    def setUp(self) -> None:
        """instantiate the Reminder objects before each test"""
        self.reminder_instance = Reminder(
            title="Test record title", description="Test record description!"
        )
        self.reminder_instance_default_kwargs = Reminder()

    def tearDown(self) -> None:
        """delete the Reminder objects after each test"""
        del self.reminder_instance
        del self.reminder_instance_default_kwargs

    def test_1_repr(self) -> None:
        """test the return of the __repr__ method"""
        self.assertEqual(
            str(self.reminder_instance),
            "<Reminder id=None, title=Test record title, description=Test record description!>",
        )

    def test_2_find_id1(self) -> None:
        """test the return of the find method for an existing id"""
        # test from instance
        self.assertEqual(
            str(self.reminder_instance.find(1)[0]),
            "<Reminder id=1, title=Mirjam is awesome, description=She is learning to code>",
        )
        # test classmethod
        self.assertEqual(
            str(Reminder.find(1)[0]),
            "<Reminder id=1, title=Mirjam is awesome, description=She is learning to code>",
        )

    def test_3_find_unknown_id(self) -> None:
        """test the return of the find method for an none existing id"""
        self.assertEqual(
            Reminder.find(100),
            (None, "il Reminder non é presente!"),
        )

    def test_4_save_id(self) -> None:
        """test the return of the save method for an valid record"""
        self.assertIn(
            "title=Test record title, description=Test record description!>",
            str(self.reminder_instance.save()),
        )
        self.assertIsInstance(self.reminder_instance.save(), Reminder)

    def test_5_save_default_kwargs(self) -> None:
        """test the return of the save method for an default instance record"""
        self.assertIn(
            "title=, description=>",
            str(self.reminder_instance_default_kwargs.save()),
        )
        self.assertIsInstance(self.reminder_instance_default_kwargs.save(), Reminder)
