from django import forms

from .models import Feedback


class FeedbackFrom(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        exclude = ["created_at"]
