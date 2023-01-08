from django.urls import path
from .views import GermanView, ReminderListView, ReminderDetailView, ReminderUpdateView, ReminderAddView, ReminderDeleteView

urlpatterns = [
    path("germany/", GermanView.as_view(), name="germany"),
    path("", ReminderListView.as_view(), name="index"),
    path("<int:pk>/", ReminderDetailView.as_view(), name="detail"),
    path("<int:pk>/update", ReminderUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", ReminderDeleteView.as_view(), name="delete"),
    path("new/", ReminderAddView.as_view(), name="new-reminder"),
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
