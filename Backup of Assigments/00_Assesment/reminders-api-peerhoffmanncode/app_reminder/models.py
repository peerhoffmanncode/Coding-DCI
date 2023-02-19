from django.db import models
from django.contrib.auth.models import User


class Reminder(models.Model):
    user = models.ForeignKey(User, related_name="reminders", on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    description = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
