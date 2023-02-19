from rest_framework import serializers
from .models import Reminder, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = [
            "id",
            "title",
            "description",
        ]


class ReminderWithUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = [
            "id",
            "user",
            "title",
            "description",
            "creation_date",
            "due_date",
        ]


class ReminderAndUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Reminder
        fields = [
            "id",
            "title",
            "description",
            "creation_date",
            "due_date",
            "user",
        ]


class UserAndReminderSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "reminders"]
