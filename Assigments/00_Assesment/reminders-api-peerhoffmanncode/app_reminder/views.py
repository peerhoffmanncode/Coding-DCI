from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics

from .models import Reminder, User
from .serializer import (
    ReminderSerializer,
    UserSerializer,
    ReminderWithUserSerializer,
    ReminderAndUserSerializer,
    UserAndReminderSerializer,
)

### Reminder related Views


class APIListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderAndUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class APICreateView(generics.CreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderWithUserSerializer


class APIRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderWithUserSerializer


### User related Views


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserAndReminderSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAndReminderSerializer
