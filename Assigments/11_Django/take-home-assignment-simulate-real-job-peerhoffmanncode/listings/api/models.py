from django.db import models
from django.utils import timezone

# DONE: Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=3, null=True)
    zipcode = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f"Location {self.pk}, in {self.city} {self.zipcode}, in {self.state}"


class House(models.Model):
    location = models.ForeignKey(
        Location, related_name="houses", on_delete=models.CASCADE
    )
    area_unit = models.CharField(max_length=10, null=True)
    bathrooms = models.FloatField(default=0.0, null=True)
    bedrooms = models.IntegerField(default=0, null=True)
    home_size = models.CharField(max_length=50, null=True)
    home_type = models.CharField(max_length=50, blank=True, null=True)
    last_sold_date = models.DateField(default=timezone.now, blank=True, null=True)
    last_sold_price = models.IntegerField(default=0, blank=True, null=True)
    link = models.URLField(max_length=200, null=True)
    price = models.CharField(max_length=50, null=True)
    property_size = models.IntegerField(default=0, null=True)
    rent_price = models.IntegerField(blank=True, null=True)
    rentzestimate_amount = models.IntegerField(default=0, null=True)
    rentzestimate_last_updated = models.DateField(default=timezone.now, null=True)
    tax_value = models.FloatField(default=0.0, null=True)
    tax_year = models.IntegerField(default=0, null=True)
    year_built = models.IntegerField(default=0, null=True)
    zestimate_amount = models.IntegerField(default=0, null=True)
    zestimate_last_updated = models.DateField(default=timezone.now, null=True)
    zillow_id = models.IntegerField(default=0, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"House {self.pk}, {self.address}, with size of {self.home_size} in {self.location.city}"
