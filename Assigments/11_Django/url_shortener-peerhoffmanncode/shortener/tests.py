from django.test import TestCase
from unittest import mock

from django.urls import reverse

from .models import Url
from .views import ShortageView, Result, RestoreView, get_random_string

from datetime import date, timedelta


# Create your tests here.
class Test(TestCase):
    def test_get_random_string(self):
        str1 = get_random_string(6)
        str2 = get_random_string(6)
        self.assertNotEqual(str1, str2)
        self.assertEqual(len(str1), 6)

    def test_shortage_view_get(self):
        response = self.client.get(reverse("shortage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("shortener/url_input.html")

    def test_shortage_view_post_duplicate(self):
        context = {"source_url": "http://www.example.com"}

        # create 5 times the same url-object!
        response = self.client.post(reverse("shortage"), context)
        first_entry = Url.objects.first()
        for i in range(4):
            response = self.client.post(reverse("shortage"), context)
        last_entry = Url.objects.last()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/result/")
        # still only 1 entry!
        self.assertEqual(len(Url.objects.all()), 1)
        self.assertEqual(first_entry, last_entry)

    # mock the function that creates the random string
    @mock.patch("shortener.views.get_random_string")
    def test_shortage_view_post_mock_surl(self, mock_random_string):
        # define a mocked return for get_random_string
        mock_random_string.return_value = "aBcDeF"
        # define the data for the post request
        context = {"source_url": "http://www.example.com"}
        # initiate a post request with mocked data
        response = self.client.post(reverse("shortage"), data=context)
        # check for a valid execution of the view
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/result/")
        # initiate a get request for the result page
        response = self.client.get(reverse("result"))
        # prove that the correct short url is shown
        self.assertIn(
            f'href="/re/{mock_random_string.return_value}"', str(response.content)
        )

    def test_restore_view_get(self):
        surl1 = get_random_string(6)
        Url.objects.create(source_url="http://www.bild.de", short_url=surl1)
        response = self.client.get(reverse("restore", kwargs={"surl": surl1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "http://www.bild.de")

    def test_restore_view_get_expired(self):
        surl2 = get_random_string(6)
        Url.objects.create(
            source_url="http://www.info.de",
            short_url=surl2,
            expires=date.today() + timedelta(days=-14),
        )
        response = self.client.get(reverse("restore", kwargs={"surl": surl2}))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Url.objects.filter(short_url=surl2).exists())
