from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, FormView

from .models import Reminder
from .forms import ReminderForm


class GermanView(TemplateView):
    template_name = "reminders/germany.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reminders"] = Reminder.objects.all()
        return context

class ReminderListView(ListView):
    template_name = "reminders/index.html"
    context_object_name = 'reminders'
    queryset = Reminder.objects.all()

    # def get_queryset(self):
    #     context = {"reminders":Reminder.objects.all()}
    #     return Reminder.objects.all()

class ReminderDetailView(DetailView):
    model = Reminder
    template_name = "reminders/detail.html"

class ReminderUpdateView(UpdateView):
    model = Reminder
    form_class = ReminderForm
    success_url = "/reminders/"
    template_name = "reminders/edit.html"

class ReminderAddView(FormView):
    model = Reminder
    form_class = ReminderForm
    success_url = "/reminders/"
    template_name = "reminders/new.html"

    def form_valid(self, form):
        if super().form_valid(form):
            form.save()
        return super().form_valid(form)

class ReminderDeleteView(DeleteView):
    model = Reminder
    success_url = "/reminders/"
    template_name = "reminders/delete.html"
