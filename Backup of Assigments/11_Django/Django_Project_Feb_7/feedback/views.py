from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Feedback
from .forms import FeedbackFrom

# Create your views here.


def list_api(request):
    feedback = [
        {"email": f.email, "message": f.message} for f in Feedback.objects.all()
    ]
    return JsonResponse({"feedback": feedback})


def list_view(request):
    feedback = Feedback.objects.all()
    return render(request, "feedback/index.html", {"feedback": feedback})


def new_feedback(request):
    if request.method == "POST":
        form = FeedbackFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("feedback:list")
    else:
        form = FeedbackFrom()
    return render(request, "feedback/new_feedback.html", {"form": form})
    # return JsonResponse({})
