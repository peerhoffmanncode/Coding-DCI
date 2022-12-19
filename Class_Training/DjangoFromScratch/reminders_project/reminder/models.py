from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    creation_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=timezone.now)

    done = models.BooleanField(default=False)
