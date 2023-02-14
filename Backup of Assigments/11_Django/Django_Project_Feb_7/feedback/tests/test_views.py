from http import HTTPStatus
from django.test import TestCase


class AddFeedbackFormTest(TestCase):
    def test_get(self):
        response = self.client.get("/new/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create feedback")

    def test_post(self):
        context = {
            "name": "Jane Doe",
            "message": "Hello world",
            "email": "jdoe@example.com",
        }
        response = self.client.post("/new/", context)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["location"], "/")
        # self.assertContains(response, "Create feedback")
