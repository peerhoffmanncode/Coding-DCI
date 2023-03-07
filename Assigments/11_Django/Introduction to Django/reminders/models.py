from django.db import models

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"this is a Reminder with title={self.title} and description={self.description}."


# Make migrations -> Translates from python to SQL
