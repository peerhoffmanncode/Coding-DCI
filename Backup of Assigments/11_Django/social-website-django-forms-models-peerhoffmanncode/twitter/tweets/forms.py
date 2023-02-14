from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Tweet


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = "__all__"
        exclude = ["user"]

    def clean(self):
        msg = self.data.get("message", None)
        if 160 > len(msg) > 0:
            return super().clean()
        raise ValidationError("Your message is not accepted")
