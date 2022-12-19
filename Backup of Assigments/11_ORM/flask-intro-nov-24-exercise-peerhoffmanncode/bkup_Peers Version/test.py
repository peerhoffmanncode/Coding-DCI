import unittest
from unittest.mock import Mock, MagicMock, patch
from flask import Flask, jsonify, request
from app import convert_reminders_format, db_read, db_write, index, add_reminder


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.app_temp_flask = Flask(__name__)

    def tearDown(self) -> None:
        # return super().tearDown()
        pass

    # Test 1 - Testing simple conversion ! Tuple to Dict method #############
    def test1(self) -> None:
        """test 1"""
        reminder_list_format = [
            ["peer", "description peer", 1],
            ["michel", "description michel", 2],
            ["fausto", "description fausto", 3],
        ]
        result = convert_reminders_format(reminder_list_format)
        expected = [
            {"title": "peer", "description": "description peer", "id": 1},
            {"title": "michel", "description": "description michel", "id": 2},
            {"title": "fausto", "description": "description fausto", "id": 3},
        ]
        self.assertEqual(result, expected)

    # Test 2 - Testing db_read method - mocking the actual reading from the db ! #############
    @patch("app.db_read", MagicMock(return_value=("Hello", "description", 1)))
    def test2(self) -> None:
        with self.app_temp_flask.app_context():
            self.assertEqual(
                index().json,
                {
                    "reminders": {
                        "description": "description",
                        "id": 1,
                        "title": "Hello",
                    }
                },
            )

    # # Test 3 - Testing db_write method - mocking the actual API call/ db_write/ db_read from the db ! #############
    # @patch(
    #     "app.request.json.get",
    #     MagicMock(side_effect=["Jim", "Joe"], autospec="request"),
    # )
    # @patch("app.request", MagicMock(autospec="request"))
    # @patch("app.db_write", MagicMock(return_value=None))
    # @patch("app.db_read", MagicMock(return_value=("Jim", "Joe!", 1)))
    # def test3(self) -> None:
    #     with self.app_temp_flask.app_context():
    #         self.assertEqual(
    #             add_reminder().json,
    #             {"reminders": {"description": "Joe!", "id": 1, "title": "Jim"}},
    #         )

    # Test 4 - Testing db_write method - mocking the actual API call/ db_write/ db_read from the db ! #############
    @patch("app.db_write")
    @patch("app.db_read")
    @patch("app.request.json.get")
    @patch("app.request")
    def test4(
        self, mock_api_request, mock_api_json, mock_db_read, mock_db_write
    ) -> None:
        with self.app_temp_flask.app_context():
            mock_db_read.return_value = ("Jim", "Joe!", 1)
            mock_db_write.return_value = None
            mock_api_request.json.get = ["Jim", "Joe"]
            #mock_api_json.side_effect = ["Jim", "Joe"]

            self.assertEqual(
                add_reminder().json,
                {"reminders": {"description": "Joe!", "id": 1, "title": "Jim"}},
            )
