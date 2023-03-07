from django.test import TestCase

from .models import Animal

# Create your tests here.
class Test(TestCase):
    def setUp(self):
        self.lion = Animal.objects.create(name="lion", sound="roar")
        self.cat = Animal.objects.create(name="cat", sound="roar")

    def test_animals_can_speak(self):
        # fetching a lion
        lion = Animal.objects.get(name="lion")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
