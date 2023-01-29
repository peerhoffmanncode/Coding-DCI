from django.db import models

# Create your models here.
class Todo(models.Model):
    description = models.TextField(blank=False)
    done = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return f"todo: {self.description}"
