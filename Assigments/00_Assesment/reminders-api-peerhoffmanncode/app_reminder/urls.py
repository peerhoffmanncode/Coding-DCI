from django.urls import path, include

from . import views

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("users/", views.UserList.as_view(), name="users-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user_detail"),
    path("reminders/", views.APIListView.as_view(), name="reminders-list"),
    path("reminders/<int:pk>/", views.APIRUDView.as_view(), name="reminders-rud"),
    path("reminders/create/", views.APICreateView.as_view(), name="reminders-create"),
]
