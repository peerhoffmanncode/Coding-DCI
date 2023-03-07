from django.core.management.base import BaseCommand, CommandError

from api.models import Location, House
import csv
import os
from datetime import datetime


def verify_data(data, should_be_type):
    """function to validate a given data object"""
    if data == "":
        return None
    try:
        if should_be_type is str:
            return data
        if should_be_type is int:
            return int(data)
        if should_be_type is float:
            return float(data)
        if should_be_type is datetime:
            return datetime.strptime(data, "%m/%d/%Y")
    except ValueError:
        return None
    else:
        return data


class Command(BaseCommand):
    help = "Imports data about houses"

    def add_arguments(self, parser):
        # TODO: Add any arguments here
        # well could have an argument to a path here.
        # but since the file is static and the only one,
        # it would be kind of over engineered then
        pass

    def handle(self, *args, **options):
        # Done: implement your import command
        path = os.getcwd() + "/../sample-data/data.csv"
        print("Importing data to database...")

        with open(path, "r") as f:
            # Read the data from the file
            reader = csv.DictReader(f)

            # Iterate over the rows
            for row in reader:
                # Create a new record in the database
                try:
                    location = Location.objects.get(
                        city=verify_data(row.get("Create_House", None), str),
                        state=verify_data(row.get("state", None), str),
                        zipcode=verify_data(row.get("zipcode", None), int),
                    )
                except Location.DoesNotExist:
                    location = Location.objects.create(
                        city=verify_data(row.get("city", None), str),
                        state=verify_data(row.get("state", None), str),
                        zipcode=verify_data(row.get("zipcode", None), int),
                    )

                house = House.objects.create(
                    location=location,
                    area_unit=verify_data(row.get("area_unit", None), str),
                    bathrooms=verify_data(row.get("bathrooms", None), float),
                    bedrooms=verify_data(row.get("bedrooms", None), int),
                    home_size=verify_data(row.get("home_size", None), int),
                    home_type=verify_data(row.get("home_type", None), str),
                    last_sold_date=verify_data(
                        row.get("last_sold_date", None), datetime
                    ),
                    last_sold_price=verify_data(row.get("last_sold_price", None), int),
                    link=verify_data(row.get("link", None), str),
                    price=verify_data(row.get("price", None), str),
                    property_size=verify_data(row.get("property_size", None), int),
                    rent_price=verify_data(row.get("rent_price", None), int),
                    rentzestimate_amount=verify_data(
                        row.get("rentzestimate_amount", None), int
                    ),
                    rentzestimate_last_updated=verify_data(
                        row.get("rentzestimate_last_updated", None), datetime
                    ),
                    tax_value=verify_data(row.get("tax_value", None), float),
                    tax_year=verify_data(row.get("tax_year", None), int),
                    year_built=verify_data(row.get("year_built", None), int),
                    zestimate_amount=verify_data(
                        row.get("zestimate_amount", None), int
                    ),
                    zestimate_last_updated=verify_data(
                        row.get("zestimate_last_updated", None), datetime
                    ),
                    zillow_id=verify_data(row.get("zillow_id", None), int),
                    address=verify_data(row.get("address", None), str),
                )
        print("done!")
