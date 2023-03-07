from django.test import TestCase
from .models import Customer

# Create your tests here.
class TestCase_Views(TestCase):
    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "banking/index.html")

    def test_add(self):
        response = self.client.get("/add-customer/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "banking/add-customer.html")

    def test_transfer(self):
        response = self.client.get("/transfer/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "banking/transfer.html")

    def test_edit(self):
        customer = Customer.objects.create(name="test_customer", amount=50000)
        response = self.client.get(f"/edit/{customer.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "banking/edit.html")

    def test_successful_transaction(self):
        customer_a = Customer.objects.create(name="Customer A", amount=1000)
        customer_b = Customer.objects.create(name="Customer B", amount=1500)

        response = self.client.post(
            "/transfer/",
            {"payer": customer_a.name, "payee": customer_b.name, "amount": 500},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)

        customer_a = Customer.objects.get(name="Customer A")
        customer_b = Customer.objects.get(name="Customer B")
        self.assertEqual(customer_a.amount, 500)
        self.assertEqual(customer_b.amount, 2000)

    def test_unsuccessful_transaction(self):
        customer_a = Customer.objects.create(name="Customer A", amount=1000)
        customer_b = Customer.objects.create(name="Customer B", amount=1500)

        response = self.client.post(
            "/transfer/",
            {"payer": customer_a.name, "payee": customer_b.name, "amount": 1500},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)

        customer_a = Customer.objects.get(name="Customer A")
        customer_b = Customer.objects.get(name="Customer B")
        self.assertEqual(customer_a.amount, 1000)
        self.assertEqual(customer_b.amount, 1500)
