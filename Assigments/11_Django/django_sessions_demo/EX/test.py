import unittest
from animal import Animal


class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.lion = Animal(name='lion', sound='roar')
        self.cat = Animal(name = 'cat', sound='meow')

    def test_animals_can_speak(self):
        self.assertEqual(self.lion.speak(), "The lion says \"roar\"")
        self.assertEqual(self.cat.speak(), "The cat says \"meow\"")
