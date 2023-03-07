from django.db import models

# Create your models here.


class Weather(models.Model):
    time = models.DateField()
    temperature = models.FloatField()
    windspeed = models.FloatField()
    winddirection = models.FloatField()
    weathercode = models.IntegerField()

    def __str__(self) -> str:
        return f"The weather @{self.time}, {self.temperature}C°, {self.windspeed}km/s."
