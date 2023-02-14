from django.db import models

# Create your models here.

class Weather(models.Model):
    temperature = models.FloatField()
    time = models.TimeField(auto_now_add=True)
    windspeed = models.FloatField()


