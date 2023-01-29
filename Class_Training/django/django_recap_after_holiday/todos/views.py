from django.shortcuts import render, redirect

# Create your views here.
from .models import Todo
from .forms import TodoForm


def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    todos = Todo.objects.all()
    form = TodoForm()
    context = {"form": form, "todos": todos}
    template = "todos/index.html"

    return render(request, template, context)
