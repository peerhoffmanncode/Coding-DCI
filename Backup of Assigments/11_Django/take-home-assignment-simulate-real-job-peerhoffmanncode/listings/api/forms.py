from django.forms import ModelForm, DateInput

from .models import Location, House


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = "__all__"


class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = "__all__"
        widgets = {
            "last_sold_date": DateInput(attrs={"type": "date"}),
            "rentzestimate_last_updated": DateInput(attrs={"type": "date"}),
            "zestimate_last_updated": DateInput(attrs={"type": "date"}),
        }
