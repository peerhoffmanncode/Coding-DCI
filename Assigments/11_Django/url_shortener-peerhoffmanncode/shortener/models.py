from django.db import models
from django.utils import timezone
from datetime import date, timedelta


# Create your models here.
class Url(models.Model):
    source_url = models.URLField(max_length=255, blank=False, null=False, unique=True)
    short_url = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateField(default=(date.today() + timedelta(days=14)))
