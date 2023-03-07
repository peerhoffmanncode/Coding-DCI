from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Reminder, User
from .serializer import ReminderAndUserSerializer

from django.utils import timezone
from django.urls import reverse

client = Client()

# these tests where originally build by ChatGPT.
# to make them work I more or less rewrote them.
# The Bot is actually nice to build the fake data, thats it.


class GetAllRemindersTest(TestCase):
    """Test module for GET all reminders API"""

    def setUp(self):
        Reminder.objects.create(
            title="Reminder 1",
            description="Description 1",
            due_date=timezone.now(),
            user=User.objects.create(username="User1"),
        )
        Reminder.objects.create(
            title="Reminder 2",
            description="Description 2",
            due_date=timezone.now(),
            user=User.objects.create(username="User2"),
        )

    def test_get_all_reminders(self):
        # get API response
        response = client.get(reverse("reminders-list"))
        # get data from db
        reminders = Reminder.objects.all()
        serializer = ReminderAndUserSerializer(reminders, many=True)
        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewReminderTest(TestCase):
    """Test module for creating a new reminder"""

    def setUp(self):
        self.valid_payload = {
            "title": "Reminder 3",
            "description": "Description 3",
            "due_date": timezone.now(),
            "user": User.objects.create(username="User3").id,
        }
        self.invalid_payload = {
            "title": "",
            "description": "Description 4",
            "due_date": "",
            "user": User.objects.create(username="User4").id,
        }

    def test_create_valid_reminder(self):
        response = client.post(
            reverse("reminders-create"),
            data=self.valid_payload,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_reminder(self):
        response = client.post(
            reverse("reminders-create"),
            data=self.invalid_payload,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleReminderTest(TestCase):
    """Test module for updating an existing reminder record"""

    def setUp(self):
        self.reminder1 = Reminder.objects.create(
            title="Reminder 4",
            description="Description 4",
            due_date=timezone.now(),
            user=User.objects.create(username="User5"),
        )
        self.valid_payload = {
            "title": "Updated Reminder 4",
            "description": "Updated Description 4",
            "due_date": timezone.now(),
            "user": User.objects.create(username="User6").id,
        }
        self.invalid_payload = {
            "title": "",
            "description": "Updated Description 4",
            "due_date": "",
            "user": User.objects.create(username="User7").id,
        }

    def test_valid_update_reminder(self):
        response = client.put(
            reverse("reminders-rud", kwargs={"pk": self.reminder1.id}),
            data=self.valid_payload,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_reminder(self):
        response = client.put(
            reverse("reminders-rud", kwargs={"pk": self.reminder1.id}),
            data=self.invalid_payload,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleReminderTest(TestCase):
    """Test module for deleting an existing reminder record"""

    def setUp(self):
        self.reminder1 = Reminder.objects.create(
            title="Reminder 5",
            description="Description 5",
            due_date=timezone.now(),
            user=User.objects.create(username="User8"),
        )

    def test_valid_delete_reminder(self):
        response = client.delete(
            reverse("reminders-rud", kwargs={"pk": self.reminder1.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
