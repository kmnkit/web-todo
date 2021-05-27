from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.views.generic import DetailView, CreateView
from .forms import TodoCreateForm
from .models import ToDo
from teams.models import Team


class TodoDetailView(DetailView):
    model = ToDo
    template_name = "todos/detail.html"
    context_object_name = "target_todo"


def create_todo(request, pk=None):
    team = Team.objects.get(pk=pk)
    form_class = TodoCreateForm(team)
    form = form_class
    if request.method == "POST":
        form = TodoCreateForm(team, request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect(reverse("todos:detail", kwargs={"pk": todo.pk}))
    return render(request, "todos/create.html", {"form": form})


# Django에서 save 할 때 update_fields 넣으면 오버헤드 예방 가능