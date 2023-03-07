import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import date, timedelta
from cloudinary import uploader
from cloudinary.models import CloudinaryField
from django.db.models import Q
import uuid

# CHOICES FOR USER
from .models_choices import (
    GENDER_CHOICES,
    COLOR_CHOICES,
    FABRIC_CHOICES,
    FABRIC_THICKNESS_CHOICES,
    BRAND_CHOICES,
    TYPE_CHOICES,
    SIZE_CHOICES,
    CONDITION_CHOICES,
    ENVIRONMENT_CHOICES,
)


class User(AbstractUser):
    # fields we inherit from AbstractUser:
    # username, password, password_conf, email, first_name, last_name,
    # joining_date, last_login, is_staff, is_active, is_superuser

    info_about = models.TextField(blank=True)
    info_birthday = models.DateField(default=timezone.now, blank=False)
    info_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=False)
    # info_gender_interest = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=False)
    location_city = models.CharField(max_length=255, blank=False)
    location_latitude = models.FloatField(blank=True, null=True)
    location_longitude = models.FloatField(blank=True, null=True)
    notification = models.BooleanField(default=True)
    social_instagram = models.URLField(
        max_length=255,
        blank=True,
        null=True,
    )
    social_facebook = models.URLField(
        max_length=255,
        blank=True,
        null=True,
    )
    social_twitter = models.URLField(
        max_length=255,
        blank=True,
        null=True,
    )
    social_spotify = models.URLField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"<User {self.first_name.title()} {self.last_name.title()} -> [{self.username}]>"

    def delete(self, *args, **kwargs):
        """Function to delete a user from the database
        make sure all UserPorfilePictures are gone too
        make sure all Sock are gone too
        """
        # delete the user profile pictures
        for profile_picture in self.profile_picture.all():
            profile_picture.delete()
        for sock in self.sock.all():
            sock.delete()
        # delete itself
        super().delete(*args, **kwargs)

    def get_age(self):
        difference = date.today() - self.info_birthday
        # Check if the difference is equal to or greater than 18 years(including leap)
        return int(round(difference.days / 365.2425, 0))

    def is_18_years(self) -> bool:
        """function the check if a user is older than 18 years"""
        difference = date.today() - self.info_birthday
        # Check if the difference is equal to or greater than 18 years(including leap)
        if round(difference.days / 365.2425, 2) >= 18:
            return True
        else:
            return False

    def to_json(self) -> dict:
        """Function to represent the model as a json dictionary
        !Important: update if changes on the model are made!"""
        return {
            "username": self.username,
            "fullname": self.get_full_name(),
            "email": self.email,
            "about": self.info_about,
            "age": self.get_age(),
            "city": self.location_city,
            "instagram": self.social_instagram,
            "facebook": self.social_facebook,
            "twitter": self.social_twitter,
            "spotify": self.social_spotify,
        }

    def get_all_pictures(self):
        """
        Function to get all profile pictures as an object list.
        Returns a queryset
        """
        return self.profile_picture.all()

    def get_picture_urls(self):
        """Function to get all profile pictures urls as a list. Returns a list"""
        return [
            profile_picture.profile_picture.url
            for profile_picture in self.profile_picture.all()
        ]

    def get_matches(self):
        """
        Function to get all user matches.
        Retrieves all UserMatch objects associated with the User instance.
        Returns a queryset
        """
        matches = UserMatch.objects.filter(Q(user=self) | Q(other=self)).exclude(
            unmatched=True
        )
        return matches

    def get_unmatched(self):
        """
        Function to get all user matches.
        Retrieves all UserMatch objects associated with the User instance.
        Returns a queryset
        """
        matches = UserMatch.objects.filter(Q(user=self) | Q(other=self)).exclude(
            unmatched=False
        )
        return matches

    def get_socks(self):
        """Retrieves all Sock objects related to the User and returns a queryset"""
        return self.sock.all()

    def get_mail_messages(self):
        """Retrieves all MessageMail objects related to the User and returns a queryset"""
        return self.mail.all()

    def get_chat_messages(self):
        """
        Retrieves all MessageChat objects associated with the User instance.
        It will check both fields user and other to see if the user is associated with the message.

        Returns:
            QuerySet: A queryset of MessageChat objects associated with the User instance
        """
        messages = MessageChat.objects.filter(Q(user=self) | Q(other=self))
        return messages


class UserProfilePicture(models.Model):
    # User.profile_picture.user.pk = User.pk  | himself
    user = models.ForeignKey(
        User, related_name="profile_picture", on_delete=models.CASCADE
    )
    # url = models.URLField(max_length=255, blank=False)
    profile_picture = CloudinaryField("profile picture")

    def delete(self, *args, **kwargs):
        """Function to delete a UserProfilePicture
        delete all pictures form the cloud as well!"""
        if self.profile_picture.public_id:
            uploader.destroy(self.profile_picture.public_id)
        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return f"<UserProfilePicture from {self.user}>"


class UserMatch(models.Model):
    # User.him.user.pk = User.pk  | himself
    # User.matched.other.objects.all() = all Other user !
    user = models.ForeignKey(User, related_name="him", on_delete=models.CASCADE)
    other = models.ForeignKey(User, related_name="matched", on_delete=models.CASCADE)
    unmatched = models.BooleanField(default=False)
    chatroom_uuid = models.UUIDField()

    def __str__(self) -> str:
        return f"<Match between {self.user} and {self.other} status {self.unmatched} chatroom_uuid {self.chatroom_uuid} >"

    def has_matches_between(self, user_instance: User, other_instance: User) -> bool:
        return (
            UserMatch.objects.filter(
                Q(user=user_instance, other=other_instance)
                | Q(user=other_instance, other=user_instance)
            ).exists()
            and not self.unmatched
        )


class Sock(models.Model):
    # User.sock.user.pk = User.pk  | himself
    user = models.ForeignKey(User, related_name="sock", on_delete=models.CASCADE)
    info_joining_date = models.DateField(auto_now_add=True, blank=False)

    info_name = models.CharField(max_length=255, blank=False)
    info_about = models.TextField(blank=True)
    info_color = models.CharField(
        max_length=10,
        choices=COLOR_CHOICES,
        blank=False,
    )
    info_fabric = models.CharField(
        max_length=20,
        choices=FABRIC_CHOICES,
        blank=False,
    )
    info_fabric_thickness = models.CharField(
        max_length=20,
        choices=FABRIC_THICKNESS_CHOICES,
        blank=False,
    )
    info_brand = models.CharField(
        max_length=30,
        choices=BRAND_CHOICES,
        blank=False,
    )
    info_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        blank=False,
    )
    info_size = models.CharField(
        max_length=20,
        choices=SIZE_CHOICES,
        blank=False,
    )
    info_age = models.PositiveSmallIntegerField(blank=False)
    info_separation_date = models.DateField(default=timezone.now, blank=False)
    info_condition = models.CharField(
        max_length=50,
        choices=CONDITION_CHOICES,
        blank=False,
    )
    info_holes = models.PositiveSmallIntegerField(blank=False)
    info_kilometers = models.PositiveSmallIntegerField(blank=False)
    info_inoutdoor = models.CharField(
        max_length=20,
        choices=ENVIRONMENT_CHOICES,
        blank=False,
    )
    info_washed = models.PositiveSmallIntegerField(blank=False)
    info_special = models.CharField(
        max_length=250,
        blank=False,
    )

    def to_json(self) -> dict:
        """Function to represent the model as a json dictionary
        !Important: update if changes on the model are made!"""
        return {
            "Name": self.info_name,
            "My story": self.info_about,
            "My specialty": self.info_special,
            "My dominant color": COLOR_CHOICES[int(self.info_color) - 1][1],
            "My fabric": FABRIC_CHOICES[int(self.info_fabric) - 1][1],
            "My fabric's thickness": FABRIC_THICKNESS_CHOICES[
                int(self.info_fabric_thickness) - 1
            ][1],
            "Lonely since": self.info_separation_date,
            "My brand": BRAND_CHOICES[int(self.info_brand) - 1][1],
            "I am a": TYPE_CHOICES[int(self.info_type) - 1][1],
            "My size": SIZE_CHOICES[int(self.info_size) - 1][1],
            "My age": self.info_age,
            "My holes": self.info_holes,
            "Kilometers I walked": self.info_kilometers,
            "My condition": CONDITION_CHOICES[int(self.info_condition) - 1][1],
            "My usage": ENVIRONMENT_CHOICES[int(self.info_inoutdoor) - 1][1],
            "How often was i washed": self.info_washed,
        }

    def get_all_pictures(self):
        """
        Retrieves all SockProfilePicture objects associated with the Sock instance.

        Returns:
            QuerySet: A queryset of SockProfilePicture objects associated with the Sock instance
        """
        profile_pictures = self.profile_picture.all()
        return profile_pictures

    def get_picture_urls(self):
        """Function to get all profile pictures urls as a list. Returns a list"""
        return [
            profile_picture.profile_picture.url
            for profile_picture in self.profile_picture.all()
        ]

    def get_likes(self):
        """
        Retrieves all Sock instances that the current Sock instance has liked.

        Returns:
            QuerySet: A queryset of Sock instances liked by the current Sock
            instance
        """
        likes = Sock.objects.filter(like__sock=self)
        return likes

    def get_dislikes(self):
        """
        Retrieves all Sock instances that the current Sock instance has
        disliked.

        Returns:
            QuerySet: A queryset of Sock instances disliked by the current Sock instance
        """
        dislikes = Sock.objects.filter(dislike__sock=self)
        return dislikes

    def __str__(self) -> str:
        return f"<Sock {self.info_name}>"

    def delete(self, *args, **kwargs):
        """Function to delete a sock from the database
        make sure all SockPorfilePictures are gone too
        """
        # delete the user profile pictures
        for profile_picture in self.profile_picture.all():
            profile_picture.delete()
        # delete itself
        super().delete(*args, **kwargs)


class SockProfilePicture(models.Model):
    # Sock.profile_picture.sock.pk = Sock.pk  | sock himself
    sock = models.ForeignKey(
        Sock, related_name="profile_picture", on_delete=models.CASCADE
    )
    # url = models.URLField(max_length=255, blank=False)
    profile_picture = CloudinaryField("profile picture")

    def __str__(self) -> str:
        return f"<SockProfilePicture from {self.sock}>"

    def delete(self, *args, **kwargs):
        """Function to delete a UserProfilePicture
        delete all pictures form the cloud as well!"""
        if self.profile_picture.public_id:
            uploader.destroy(self.profile_picture.public_id)

        super().delete(*args, **kwargs)


class SockLike(models.Model):
    # Sock.me.sock.pk = Sock.pk  | sock himself
    # Sock.like.like.objects.all() = socks i like
    # Sock.dislike.dislike.objects.all() = socks i don't like
    sock = models.ForeignKey(
        Sock, related_name="me", on_delete=models.CASCADE, blank=False
    )
    like = models.ForeignKey(
        Sock,
        related_name="like",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    dislike = models.ForeignKey(
        Sock,
        related_name="dislike",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"<SockLike for {self.sock}>"


class MessageMail(models.Model):
    # User.mail.user.pk = User.pk  | user himself
    user = models.ForeignKey(User, related_name="mail", on_delete=models.CASCADE)
    subject = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    sent_date = models.DateField(auto_now_add=True, blank=False)

    def __str__(self) -> str:
        return f"<Mail from {self.user} Subject: {self.subject} @{self.sent_date}>"


class MessageChat(models.Model):
    # User.chat_sending.user.pk = User.pk  | user himself
    # User.chat_receiving.other.objects.all() = user send to !
    user = models.ForeignKey(
        User, related_name="chat_sending", on_delete=models.CASCADE
    )
    other = models.ForeignKey(
        User, related_name="chat_receiving", on_delete=models.CASCADE
    )
    message = models.CharField(max_length=255, blank=False)
    sent_date = models.DateTimeField(auto_now_add=True, blank=False)
    seen_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        if self.seen_date:
            return f"<Chat from {self.user} to {self.other} Subject: {self.message} sent@{self.sent_date.time()} / seen@{self.seen_date.time()}>"
        else:
            return f"<Chat from {self.user} to {self.other} Subject: {self.message} sent@{self.sent_date.time()} / UNSEEN YET!"
