from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(User, related_name="tweets", on_delete=models.CASCADE)
    message = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
