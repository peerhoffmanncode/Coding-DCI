from django.core.management.base import BaseCommand, CommandError

from core.models import Weather

import requests
from datetime import datetime


class Command(BaseCommand):
    help = "find weather data using an API"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "total", type=int, help="Indicates the number of users to be created"
    #     )

    def handle(self, *args, **kwargs):
        # fixed location for mainz
        latitude = 50.11088
        longitude = 8.681996

        # design api url
        request_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=True"
        # request data form api
        response = requests.get(request_url).json()["current_weather"]

        db_record = Weather.objects.create(
            time=datetime.strptime(response["time"], "%Y-%m-%dT%H:%M"),
            temperature=response["temperature"],
            windspeed=response["windspeed"],
            winddirection=response["winddirection"],
            weathercode=response["weathercode"],
        )
        print(db_record)
