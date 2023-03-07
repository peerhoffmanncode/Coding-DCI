from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewset(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    # TODO: Order_by SQL and use it in Django

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated]


class GroupViewset(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
