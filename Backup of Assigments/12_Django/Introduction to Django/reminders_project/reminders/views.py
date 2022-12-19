from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Reminder
import json


def index(request):
    reminders = Reminder.objects.all()
    context = {
        "reminders": [
            {"id": r.pk, "title": r.title, "description": r.description}
            for r in reminders
        ]
    }
    return JsonResponse(context)
    # return render(request, "reminders/index.html", context)


@csrf_exempt
def new_reminder(request):

    data = json.loads(request.body)
    # print(dir(request))
    title = data.get("title")
    description = data.get("description")
    new_reminder_record = Reminder.objects.create(title=title, description=description)

    reminder_dict = {
        "id": new_reminder_record.pk,
        "title": new_reminder_record.title,
        "description": new_reminder_record.description,
    }
    return JsonResponse(reminder_dict)
