from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

# from django.urls import reverse
from django.views.generic import (
    TemplateView,
    DetailView,
    FormView,
    UpdateView,
    DeleteView,
)
from .models import Location, House
from .forms import HouseForm, LocationForm

# DONE: Create your views here. ??? I guess
class LocationsListView(TemplateView):
    template_name = "api/list_locations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = Location.objects.all()
        return context


class HousesListView(TemplateView):
    template_name = "api/list_houses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location = Location.objects.get(pk=kwargs.get("pk"))
        context["location"] = location
        context["houses"] = location.houses.all()
        return context


class HouseDetailView(DetailView):
    model = House
    template_name = "api/detail_house.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location = get_object_or_404(Location, pk=self.kwargs["pk"])
        context["location"] = location
        context["house"] = location.houses.get(pk=self.kwargs["house_pk"])
        return context


class LocationCreate(FormView):

    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("location-list")
    template_name = "api/new_location.html"

    def form_valid(self, form):
        if super().form_valid(form):
            form.save()
        return super().form_valid(form)


class LocationEdit(UpdateView):

    model = Location
    form_class = LocationForm
    template_name = "api/update_location.html"

    def get_success_url(self):
        # Reverse the URL and pass in the pk of the updated object
        return reverse("houses-list", kwargs={"pk": self.object.pk})


class LocationDelete(DeleteView):

    model = Location
    form_class = LocationForm
    template_name = "api/delete_location.html"

    def get_success_url(self):
        # Reverse the URL and pass in the pk of the updated object
        return reverse("location-list")


class HouseCreate(FormView):

    model = House
    form_class = HouseForm
    success_url = "stuff"  # Wired ?! Needs to be truthy ???
    template_name = "api/new_house.html"

    def get_initial(self):
        initial = super().get_initial()
        initial["location"] = Location.objects.get(pk=self.kwargs["pk"])
        return initial

    def form_valid(self, form):
        if super().form_valid(form):
            orm_object = form.save()
        return redirect(reverse("houses-list", kwargs={"pk": orm_object.location.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["initial"] = self.get_initial()
        return context


class HouseEdit(UpdateView):

    model = House
    form_class = HouseForm
    # success_url = "/api/locations/"
    template_name = "api/update_house.html"

    def get_object(self, queryset=None):
        return get_object_or_404(
            House, pk=self.kwargs["house_id"], location__pk=self.kwargs["pk"]
        )

    def get_success_url(self):
        # Reverse the URL and pass in the pk of the updated object
        return reverse(
            "house-detail",
            kwargs={"pk": self.object.location.pk, "house_pk": self.object.pk},
        )


class HouseDelete(DeleteView):

    model = House
    form_class = HouseForm
    success_url = ""
    template_name = "api/delete_House.html"

    def get_object(self, queryset=None):
        return get_object_or_404(
            House, pk=self.kwargs["house_id"], location__pk=self.kwargs["pk"]
        )

    def get_success_url(self):
        # Reverse the URL and pass in the pk of the updated object
        return reverse("houses-list", kwargs={"pk": self.object.location.pk})
