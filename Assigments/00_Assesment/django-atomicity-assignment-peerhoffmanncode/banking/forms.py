from .models import Customer
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("name", "amount")
        labels = {"name": "Customer name", "amount": "Amount in [€]"}


class TransferForm(forms.Form):
    # payer = forms.CharField(label="Payer", max_length=255, required=True)
    # payee = forms.CharField(label="Payee", max_length=255, required=True)
    # amount = forms.IntegerField(label="Transfer amount [€]", required=True)

    # Create a model choice field with the Select widget
    payer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.Select,
        required=True,
    )
    payee = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.Select,
        required=True,
    )
    amount = forms.IntegerField(label="Transfer amount [€]", required=True)
