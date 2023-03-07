from django.test import TestCase
from django.urls import reverse
from django.shortcuts import resolve_url
from .models import Reminder


class DeleteItemTest(TestCase):
    def test_delete_item(self):
        Reminder.objects.create(title="Test", description="test")
        url = "/reminders/1/delete"
        response = self.client.delete(f"{url}")
        print(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content, b'{"message": "Successfully deleted"}')


class MathTest(TestCase):
    def test_addition_operation(self):
        url = reverse("math")
        response = self.client.get(f"{url}?operation=add&a=1&b=2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "3")

    def test_subtraction_operation(self):
        url = reverse("math")
        response = self.client.get(f"{url}?operation=sub&a=1&b=2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "-1")

    def test_multi_operation(self):
        url = reverse("math")
        response = self.client.get(f"{url}?operation=mul&a=3&b=2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "6")

    def test_div_operation1(self):
        url = reverse("math")
        response = self.client.get(f"{url}?operation=div&a=6&b=2")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "3")

    def test_div_operation2(self):
        url = reverse("math")
        response = self.client.get(f"{url}?operation=div&a=6&b=0")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content, b'{"result": "ERROR!"}')
