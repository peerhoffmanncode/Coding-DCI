from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Reminder
from .forms import ReminderForm

# Create your views here.
# CRUD !
# List of thing
# Detail of that one thing
# new things (new reminder)
# editing a reminder
# delete that reminder


def list_of_reminders(request):
    # get all the reminders
    reminders = Reminder.objects.all()

    # render the reminders in a template

    return render(request, "reminders/index.html", {"reminders": reminders})


def new_reminder(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)
        # check if the for mis valid
        if form.is_valid():
            # title = form.cleaned_data["title"]
            # description = form.cleaned_data["description"]
            # creates an object and stores it in the database
            # Reminder.objects.create(title=title, description=description)
            form.save()
            return redirect(reverse("index"))

    else:
        form = ReminderForm()

    return render(request, "reminders/new.html", {"form": form})


def detail(request, reminder_id):
    # get all the reminders
    reminder = get_object_or_404(Reminder, pk=reminder_id)

    # render the reminders in a template

    return render(request, "reminders/detail.html", {"reminder": reminder})


def update(request, reminder_id):
    # get all the reminders
    reminder = get_object_or_404(Reminder, pk=reminder_id)

    form = ReminderForm(
        initial={"title": reminder.title, "description": reminder.description}
    )
    if request.method == "POST":
        form = ReminderForm(request.POST, instance=reminder)
        # check if the for mis valid
        if form.is_valid():

            form.save()
            return redirect(reverse("detail", kwargs={"reminder_id": reminder_id}))

    return render(request, "reminders/edit.html", {"reminder": reminder, "form": form})
