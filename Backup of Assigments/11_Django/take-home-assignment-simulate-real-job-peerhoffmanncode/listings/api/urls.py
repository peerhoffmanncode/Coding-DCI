from django.urls import include, path

from .views import (
    LocationsListView,
    HousesListView,
    HouseDetailView,
    HouseCreate,
    HouseEdit,
    HouseDelete,
    LocationCreate,
    LocationEdit,
    LocationDelete,
)

# DONE: Create your routers and urls here
urlpatterns = [
    path("", LocationsListView.as_view(), name="location-list"),
    path("<int:pk>/houses/", HousesListView.as_view(), name="houses-list"),
    path(
        "create-location/",
        LocationCreate.as_view(),
        name="location-create",
    ),
    path(
        "<int:pk>/edit-location/",
        LocationEdit.as_view(),
        name="location-edit",
    ),
    path(
        "<int:pk>/delete-location/",
        LocationDelete.as_view(),
        name="location-delete",
    ),
    path(
        "<int:pk>/houses/<int:house_pk>",
        HouseDetailView.as_view(),
        name="house-detail",
    ),
    path(
        "<int:pk>/create-house/",
        HouseCreate.as_view(),
        name="house-create",
    ),
    path(
        "<int:pk>/houses/<int:house_id>/edit-house/",
        HouseEdit.as_view(),
        name="house-edit",
    ),
    path(
        "<int:pk>/houses/<int:house_id>/delete-house/",
        HouseDelete.as_view(),
        name="house-delete",
    ),
]
