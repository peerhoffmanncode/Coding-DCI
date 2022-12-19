from django.test import TestCase
from .forms import CustomerForm, TransferForm

# Create your tests here.
class TestCase_Forms(TestCase):
    def test_CustomerForms_missing_name(self):
        form = CustomerForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())

    def test_CustomerForms_correctly_set(self):
        form = CustomerForm({"name": "Test", "amount": 1000})
        self.assertTrue(form.is_valid())

    def test_TransferForms_missing_name(self):
        form = TransferForm({"payer": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("payer", form.errors.keys())

    def test_TransferForms_correctly_set(self):
        form = TransferForm({"payer": "TestA", "payee": "TestB", "amount": 1000})
        self.assertTrue(form.is_valid())
