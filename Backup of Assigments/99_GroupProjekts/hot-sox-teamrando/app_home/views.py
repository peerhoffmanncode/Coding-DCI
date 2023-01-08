from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# from django.contrib.auth.models import User
from app_users.models import User


def home(request):
    # breakpoint()
    if request.user.username:
        user = User.objects.get(username=request.user.username)
        user.username = user.username.title()
        context = {"user": user}
    else:
        context = {"user": None}

    return render(request, "app_home/index.html", context)


# @login_required(login_url="/user/login")
def prove_of_concept(request):
    if request.user.is_authenticated:
        # The user is logged in
        return HttpResponse(
            f'<h1>Seems like you are logged in! Yeay! </h1><p>Nice job {str(request.user.username).title()}!</p><br><a href="/">return to home</a>'
        )
    else:
        # The user is not logged in
        return HttpResponse(
            '<h1>Please first log in to access this page.</h1><br><a href="/user/login">Sign in</a>'
        )
