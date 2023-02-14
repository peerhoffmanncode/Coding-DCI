from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.views.generic import TemplateView

from .forms import TweetForm
from .models import Tweet

# Create your views here.


class CreateTweet(TemplateView):
    def get(self, request, *args, **kwargs):
        form = TweetForm()
        context = {"form": form, "user": request.user}
        return render(request, "tweets/create-tweet.html", context)

    def post(self, request, *args, **kwargs):
        form = TweetForm(request.POST)

        if form.is_valid():
            tweet = form.save(commit=False)
            # add user to tweet
            tweet.user = request.user
            tweet.save()
            return render(request, "tweets/show-tweet.html", {"tweet": tweet})
        return redirect(reverse("create-tweet"))

class DeleteTweet(TemplateView):
    def get(self, request, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=kwargs['pk'])
        tweet.delete()
        return redirect(reverse('home'))

class UpdateTweet(TemplateView):
    def get(self, request, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=kwargs['pk'])
        form = TweetForm(instance=tweet)
        context = {"form": form, "user": request.user}
        return render(request, "tweets/create-tweet.html", context)

    def post(self, request, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=kwargs['pk'])
        form = TweetForm(request.POST, instance=tweet )

        if form.is_valid():
            tweet = form.save(commit=False)
            # add user to tweet
            tweet.user = request.user
            tweet.save()

        return render(request, "tweets/show-tweet.html", {"tweet": tweet})
