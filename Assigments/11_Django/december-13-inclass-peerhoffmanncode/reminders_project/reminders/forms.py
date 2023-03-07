from django import forms
from .models import Reminder


class ReminderForm(forms.ModelForm):
    # fields / columns of reminder table
    class Meta:
        model = Reminder
        fields = ("title", "description")


# class ReminderForm(forms.Form):
#     # fields / columns of reminder table
#     title = forms.CharField(label="Title", max_length=255, required=True)
#     description = forms.CharField(label="Description", widget=forms.Textarea)
