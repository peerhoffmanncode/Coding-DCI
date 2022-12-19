from django.db import models
from django import forms

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"title: {self.title}"

    def to_json(self):
        return {"id": self.pk, "title": self.title, "description": self.description}


class ReminderForm(forms.ModelForm):
    # fields / columns of reminder table
    class Meta:
        model = Reminder
        fields = ("title", "description")


# class ReminderForm(forms.Form):
#     # fields / columns of reminder table

#     title = forms.CharField(label="Title", max_length=255, required=True)
#     description = forms.CharField(label="Description", widget=forms.Textarea)
