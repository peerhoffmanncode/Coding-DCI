import unittest
import json
from app import HamburgRailExchangeScheduler
from tools import time_to_minutes
import os.path


class NoAPI_HamburgRailExchangeScheduler(HamburgRailExchangeScheduler):
    def get_city_data(self):
        """Download data from other cities. WARNING: This method makes an external API call!
        changed for the sake of the test ! :-)"""
        data = {}
        for city in ["berlin", "bremen", "kiel", "leipzig", "munich"]:
            # print(f"Opening file form /DATA for {city}.")
            with open(f"../data/{city}.json") as f:
                data[city] = json.loads(f.read())
        return data

    def notify_city(self, city, message):
        """Send message about change to another city. WARNING: This method makes an external API call!
        passed for the sake of the test ! :-)"""
        pass
        # urllib.request.Request(f"{EXTERNAL_URL}{city}/", data=json.dumps(message))


class SchedulerTest(unittest.TestCase):
    def setUp(self):
        self.NoAPIClass = NoAPI_HamburgRailExchangeScheduler()

    def test_1(self):
        """bremen to hamburg 15:33 - 16:30"""
        self.assertEqual(
            self.NoAPIClass.schedule_train_from_hamburg("bremen", "15:33"),
            ("15:34", "16:30"),
        )

    def test_2(self):
        train_1, _ = self.NoAPIClass.schedule_train_to_hamburg("bremen", "16:15")
        train_1_minutes = time_to_minutes(train_1)
        train_2, _ = self.NoAPIClass.schedule_train_to_hamburg("bremen", "16:15")
        train_2_minutes = time_to_minutes(train_2)
        train_3, _ = self.NoAPIClass.schedule_train_to_hamburg("bremen", "16:15")
        train_3_minutes = time_to_minutes(train_3)
        train_4, _ = self.NoAPIClass.schedule_train_to_hamburg("bremen", "16:15")
        train_4_minutes = time_to_minutes(train_4)
        self.assertTrue(
            (train_1_minutes != train_2_minutes)
            and (abs(train_1_minutes - train_2_minutes) >= 15)
        )
        self.assertTrue(
            (train_2_minutes != train_3_minutes)
            and (abs(train_2_minutes - train_3_minutes) >= 15)
        )
        self.assertTrue(
            (train_3_minutes != train_4_minutes)
            and (abs(train_3_minutes - train_4_minutes) >= 15)
        )
        self.assertTrue(
            (train_4_minutes != train_1_minutes)
            and (abs(train_4_minutes - train_1_minutes) >= 15)
        )

    def test_3(self):
        departure, _ = self.NoAPIClass.schedule_train_to_hamburg("leipzig", "23:51")
        self.assertEqual(departure[:-3], "00")

    def test_4(self):
        for city in ["berlin", "bremen", "kiel", "leipzig", "munich"]:
            self.assertTrue(os.path.exists(f"../data/{city}.json"))


if __name__ == "__main__":
    unittest.main()
