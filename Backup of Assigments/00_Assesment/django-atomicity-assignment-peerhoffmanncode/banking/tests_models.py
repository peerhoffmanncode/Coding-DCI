from django.test import TestCase
from .models import Customer
from datetime import datetime, date

# Create your tests here.
class TestCase_Models(TestCase):
    def test_str_method(self):
        customer = Customer.objects.create(name="test_customer", amount=50000)
        self.assertEqual(
            f"Test_Customer with a ballance of 500.0€, joined at {date.today()}",
            str(customer),
        )

    def test_date(self):
        customer = Customer.objects.create(name="test_customer", amount=50000)
        self.assertEqual(date.today(), customer.joining_date)
