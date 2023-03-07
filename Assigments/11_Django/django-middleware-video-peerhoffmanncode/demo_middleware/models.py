from django.db import models

# Create your models here.
class NewStats(models.Model):

    win = models.IntegerField()
    mac = models.IntegerField()
    linux = models.IntegerField()
    other = models.IntegerField()
