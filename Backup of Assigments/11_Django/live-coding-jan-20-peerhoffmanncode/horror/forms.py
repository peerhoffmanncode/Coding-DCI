from django import forms

CHOICES = (
    ("aquarius", "Aquarius"),
    ("pisces", "Pisces"),
    ("aries", "Aries"),
    ("taurus", "Taurus"),
    ("gemini", "Gemini"),
    ("cancer", "Cancer"),
    ("leo", "Leo"),
    ("virgo", "Virgo"),
    ("libra", "Libra"),
    ("scorpio", "Scorpio"),
    ("sagittarius", "Sagittarius"),
    ("capricorn", "Capricorn"),
)


class ZodiacForm(forms.Form):
    # sign = forms.CharField(label="Your sign")
    select = forms.ChoiceField(
        required=False, choices=CHOICES, label="Select your sign"
    )
