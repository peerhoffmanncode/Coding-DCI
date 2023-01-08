from django.test import TestCase
from .models import Location, House

# DONE: Create your tests here.


class MainViewTestCase(TestCase):
    def setUp(self):
        self.location_1 = Location.objects.create(
            city="Seattle",
            state="WA",
            zipcode=98104,
        )
        self.houses_1 = House.objects.create(
            location=self.location_1,
            area_unit="sqft",
            home_size="2000",
            home_type="Single Family",
            last_sold_date="2020-01-01",
            last_sold_price=500000,
            link="https://www.example.com",
            price="$500000",
            property_size=10000,
            year_built=1990,
            address="123 Main St",
        )
        self.location_2 = Location.objects.create(
            city="Austin",
            state="TX",
            zipcode=87654,
        )
        self.houses_2 = House.objects.create(
            location=self.location_2,
            area_unit="sqft",
            home_size="3000",
            home_type="Single Family",
            last_sold_date="2010-01-01",
            last_sold_price=300000,
            link="https://www.example2.com",
            price="$100000",
            property_size=15000,
            year_built=1890,
            address="456 Main St",
        )
        self.location_3 = Location.objects.create(
            city="Mianz",
            state="RLP",
            zipcode=55118,
        )
        self.houses_3 = House.objects.create(
            location=self.location_3,
            area_unit="sqft",
            home_size="3000",
            home_type="Single Family",
            last_sold_date="2010-01-01",
            last_sold_price=300000,
            link="https://www.example2.com",
            price="$100000",
            property_size=15000,
            year_built=1890,
            address="Wallaustr. 42",
        )

    def test_view_renders_template(self):
        # Issue a GET request to the view
        response = self.client.get("/api/locations/")
        # Check that the view is rendering the correct template
        self.assertTemplateUsed(response, "api/list_locations.html")

    def test_view_passes_all_locations(self):
        # Issue a GET request to the view
        response = self.client.get("/api/locations/")

        # Check that the view is passing all locations to the template
        self.assertEqual(
            list(response.context["locations"]),
            [self.location_1, self.location_2, self.location_3],
        )

    def test_view_renders_template1(self):
        # Issue a GET request to the view
        response = self.client.get("/api/locations/1/houses/")
        # Check that the view is rendering the correct template
        self.assertTemplateUsed(response, "api/list_houses.html")

    def test_view_renders_template2(self):
        # Issue a GET request to the view
        response = self.client.get("/api/locations/1/houses/1")
        # Check that the view is rendering the correct template
        self.assertTemplateUsed(response, "api/detail_house.html")

    def test_view_passes_correct_house1(self):
        # Issue a GET request to the view
        response = self.client.get("/api/locations/1/houses/1")
        # Check that the view is passing the correct house to the template
        self.assertEqual(str(response.context["house"]), str(self.houses_1))

    def test_view_passes_correct_house2(self):
        # Issue a GET request to the view
        response = self.client.get("/api/locations/2/houses/2")  # 2/houses/1")
        # Check that the view is passing the correct house to the template
        self.assertEqual(str(response.context["house"]), str(self.houses_2))

    def test_model_str_representation(self):
        # Check that the __str__ method returns the expected string
        self.assertEqual(
            str(self.houses_1),
            "House 1, 123 Main St, with size of 2000 in Seattle",
        )
