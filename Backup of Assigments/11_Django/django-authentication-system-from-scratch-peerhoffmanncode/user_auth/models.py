from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class AuthUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
