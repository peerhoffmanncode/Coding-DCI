from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import transaction
from .models import Customer
from .forms import CustomerForm, TransferForm

# Create your views here.
def index(request):
    """Route to the index page of the bank"""
    customers = Customer.objects.all()
    formated_customer = []
    for customer in customers:
        formated_customer.append(customer.to_json())
    return render(request, "banking/index.html", {"customers": formated_customer})


def edit(request, pk):
    """Route to an edit function for a given customer"""
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        try:
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                return redirect(reverse("index"))
        except Exception as err:
            print("LOG: Error during customer edit!", err)

    form = CustomerForm(instance=customer)
    context = {"form": form}
    return render(request, "banking/edit.html", context)


def add(request):
    """Route to add a customer"""
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))

    form = CustomerForm()
    context = {"form": form}
    return render(request, "banking/add-customer.html", context)


def transfer(request):
    """Route to initiate a transfer of money between customers"""
    if request.method == "POST":
        form = TransferForm(request.POST)
        # breakpoint()
        if form.is_valid():
            payer = form.cleaned_data.get("payer")
            payee = form.cleaned_data.get("payee")
            amount = form.cleaned_data.get("amount")

            if (
                amount
                and payer
                and payee
                and (payer.pk != payee.pk and payer.name != payee.name)
            ):
                # converting amount from euro to cent!
                # amount = amount * 100

                with transaction.atomic():
                    # get payer and payee from db
                    try:
                        payer_object = Customer.objects.get(
                            pk=payer.pk, name=payer.name
                        )
                        # only process if payer has enough money!
                        if payer_object.amount >= amount:
                            payer_object.amount -= amount
                            payer_object.save()

                            payee_object = Customer.objects.get(
                                pk=payee.pk, name=payee.name
                            )
                            payee_object.amount += amount
                            payee_object.save()
                        else:
                            raise ValueError(
                                f"{payer_object.name} has not enough money!"
                            )
                    except Exception as err:
                        print("LOG: Unaccepted transaction!", err)

            return redirect(reverse("index"))

    form = TransferForm()
    context = {"form": form}
    return render(request, "banking/transfer.html", context)
