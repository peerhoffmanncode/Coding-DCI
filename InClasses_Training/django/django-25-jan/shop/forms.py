# import the forms module

from django import forms
from django.core.exceptions import ValidationError

from better_profanity import profanity
# inherit from forms.Form

# organization
CAR_CHOICES = (
    ('bmw', "BMW"),
    ('tesla', "Tesla"),
    ('fiat', "Fiat"),
    ('audi', "Audi"),
)

class CarSearch(forms.Form):
    start_date = forms.DateField(label='When do you want to take car?', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='when to bring back car?', widget=forms.SelectDateWidget)
    cars = forms.CharField(initial="fiat", label="Choose your car", widget=forms.Select(choices=CAR_CHOICES), help_text="All our cars are premium, if you scratch you pay!")


class SearchForm(forms.Form):
    # TODO: add date support e.g. when money should arrive to the person you are sending it to.
    search_term = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)

class HotelSearch(forms.Form):
    start_date = forms.DateField(label='Checkin', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Checkout', widget=forms.SelectDateWidget)

def validate_email_NK(value):
    if value.endswith('.np'):
        raise ValidationError("Sorry, you are not allowed to send emails to North Korea!")

def validate_email_curse(value):
    profanity.load_censor_words()
    if profanity.contains_profanity(value):
            raise ValidationError("Sorry, you are not allowed to use curse words!")

def validate_email_problems(value):
    PROBLEMATIC_PHRASES = ["kill my self", "bomb", "country music"]
    for curse in PROBLEMATIC_PHRASES:
        if curse in value:
            raise ValidationError("Dude, you need some help!")

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(validators=[validate_email_NK, validate_email_curse, validate_email_problems]) # some validations in frontend
    reason = forms.CharField(widget=forms.Textarea)
