from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import View, FormView
from .forms import LoginForm

from .models import AuthUser

class ShopView(View):

    def get(self, request):
        if self.request.session.get("user_id", None):
            return render(request, "user_auth/shop.html")
        return redirect(reverse_lazy("login"))


class HomeView(View):

    def get(self, request):
        return render(request, "user_auth/home.html")


class SignUpView(FormView):
    template_name = "user_auth/signup.html"
    form_class = LoginForm
    success_url = reverse_lazy("shop")

    def get(self, request):
        if self.request.session.get("user_id", None):
            # The user is already authenticated
            # No need to proceed with the login
            return HttpResponseRedirect(self.success_url)
        else:
            # The user is not authenticated
            # We proceed with the login
            return super().get(request)

    def form_valid(self, form):

        username = form.data.get("username", None)
        password = form.data.get("password", None)
        if username and password:
            user = AuthUser.objects.create(username=username, password=password)
            # Flush the session to generate a new sessionid
            self.request.session.flush()
            # Set the session data
            self.request.session["user_id"] = username
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)

class LoginView(FormView):
    template_name = "user_auth/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("shop")

    def get(self, request):
        if self.request.session.get("user_id", None):
            # The user is already authenticated
            # No need to proceed with the login
            return HttpResponseRedirect(self.success_url)
        else:
            # The user is not authenticated
            # We proceed with the login
            return super().get(request)

    def form_valid(self, form):
        username = form.data.get("username", None)
        password = form.data.get("password", None)

        try:
            user = AuthUser.objects.get(username=username)
            if user:
                if username == user.username and password == user.password:
                    # Flush the session to generate a new sessionid
                    self.request.session.flush()
                    # Set the session data
                    self.request.session["user_id"] = username
                    # Go back to the shop
                    return HttpResponseRedirect(self.success_url)
        except AuthUser.DoesNotExist:
            pass
        return super().form_valid(form)


class LogoutView(View):

    def dispatch(self, request):
        self.request.session.flush()
        return HttpResponseRedirect(reverse("home"))
