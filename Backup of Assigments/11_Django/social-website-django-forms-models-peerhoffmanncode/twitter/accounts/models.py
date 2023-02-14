from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        primary_key=True,
        verbose_name="user",
        related_name="profile",
        on_delete=models.CASCADE,
    )
    bio = models.TextField(max_length=255, blank=True, null=True)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")

    def __str__(self):
        print(type(self.followers), self.followers)
        if self.followers.all():
            return f"[{self.user.username}] which has {len(self.followers.all())} followers"
        return f"[{self.user.username}] with no followers"
