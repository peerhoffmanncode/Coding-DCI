from django.views.generic import TemplateView, View
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings

from .forms import FollowForm


class ProfileView(TemplateView):
    def get(self, request):
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        followers = user_profile.followers.all()
        user_profiles = UserProfile.objects.exclude(user=user)

        for follower in followers:
            user_profiles = user_profiles.exclude(user=follower)


        return render(
            request,
            "accounts/profile.html",
            {
                "followers": followers,
                "user_profiles": user_profiles,
            },
        )

    def post(self, request):
        user = request.user
        user_profile = UserProfile.objects.get(user=user)


        if request.POST.get("follow"):
            follower_user = get_object_or_404(User, username=request.POST.get("follow"))
            user_profile.followers.add(follower_user)
            user_profile.save()
            send_mail (f"Hooray a new follower, {follower_user.username}", "A new follower was added! :-)", settings.EMAIL_HOST_USER,[request.user.email])
            send_mail (f"Hooray someone follows you: {request.user.username}", f"{request.user.username} is interessted in your tweets!", settings.EMAIL_HOST_USER,[follower_user.email])

        if request.POST.get("unfollow"):
            unfollower_user = get_object_or_404(
                User, username=request.POST.get("unfollow")
            )
            user_profile.followers.remove(unfollower_user)
            user_profile.save()
            # we do no send emails for this ... to sad to tell the truth ... ;)


        # End of task (do not touch code below)
        followers = user_profile.followers.all()
        user_profiles = UserProfile.objects.exclude(user=user)
        for follower in followers:
            user_profiles = user_profiles.exclude(user=follower)

        return render(
            request,
            "accounts/profile.html",
            {"followers": followers, "user_profiles": user_profiles},
        )
