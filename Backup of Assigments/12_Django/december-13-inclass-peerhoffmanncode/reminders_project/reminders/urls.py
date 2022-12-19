from django.urls import path
from . import views

# This is valid - below
# from .views import  index, new_reminder

urlpatterns = [
    path("", views.list_of_reminders, name="index"),
    path("new/", views.new_reminder, name="new-reminder"),
    path("<int:reminder_id>/", views.detail, name="detail"),
    path("<int:reminder_id>/update", views.update, name="update"),
]

# URL designs+
# CRUD
# /reminders (/noun(plural))
# one item
# /reminders/1

# Edit url
# /reminders/1/edit -> add a verb

# Delete url
# /reminder/1/delete -> remove
