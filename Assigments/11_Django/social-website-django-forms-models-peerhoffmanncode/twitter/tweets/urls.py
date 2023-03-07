from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateTweet.as_view(), name="create-tweet"),
    path("<int:pk>/delete/", views.DeleteTweet.as_view(), name="delete-tweet"),
    path("<int:pk>/update/", views.UpdateTweet.as_view(), name="update-tweet"),
]
