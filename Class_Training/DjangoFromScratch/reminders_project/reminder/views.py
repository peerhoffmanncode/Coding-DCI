from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Reminder
from .forms import ReminderForm


def homer(request):
    # showing all the Reminders
    all_reminders = Reminder.objects.all()
    context = {"reminders": all_reminders}
    return render(request, "reminder/index.html", context)


def bart(request):
    # add a Reminder

    if request.method == "POST":

        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
        else:
            print("EEEEERRRROOOOOR!")

    form = ReminderForm()
    context = {"form": form}
    return render(request, "reminder/add.html", context)


def lisa(request, pk):
    # update a Reminder
    reminder_instance = Reminder.objects.get(pk=pk)

    if request.method == "POST":
        form = ReminderForm(request.POST, instance=reminder_instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
        else:
            print("EEEEERRRROOOOOR!")

    form = ReminderForm(instance=reminder_instance)
    context = {"form": form}
    return render(request, "reminder/update.html", context)


def barny(request, pk):
    # delete a the Reminder
    reminder_instance = Reminder.objects.get(pk=pk)
    reminder_instance.delete()
    return redirect(reverse("index"))
