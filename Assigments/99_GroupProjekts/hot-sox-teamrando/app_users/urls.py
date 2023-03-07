from django.urls import path
from . import views

app_name = "app_users"
urlpatterns = [
    path("signup/", views.UserSignUp.as_view(), name="user-signup"),
    path(
        "profile/details/",
        views.UserProfileDetails.as_view(),
        name="user-profile-details",
    ),
    path(
        "profile/update/",
        views.UserProfileUpdate.as_view(),
        name="user-profile-update",
    ),
    path(
        "profile/picture/",
        views.UserProfilePictureUpdate.as_view(),
        name="user-profile-picture",
    ),
    path(
        "profile/matches/",
        views.UserMatches.as_view(),
        name="user-matches",
    ),
    path(
        "match/details/<str:username>/",
        views.UserMatchProfileDetails.as_view(),
        name="user-match-profile-details",
    ),
    path(
        "match/delete/<str:username>/",
        views.UserMatchDelete.as_view(),
        name="user-match-delete",
    ),
    path(
        "sock/overview/",
        views.SockProfileOverview.as_view(),
        name="sock-overview",
    ),
    path(
        "sock/select/",
        views.SockSelection.as_view(),
        name="sock-selection",
    ),
    path(
        "sock/details/",
        views.SockProfileDetails.as_view(),
        name="sock-details",
    ),
    path(
        "sock/create/",
        views.SockProfileCreate.as_view(),
        name="sock-create",
    ),
    path(
        "sock/update/",
        views.SockProfileUpdate.as_view(),
        name="sock-update",
    ),
    path(
        "sock/picture/",
        views.SockProfilePictureUpdate.as_view(),
        name="sock-picture",
    ),
]
