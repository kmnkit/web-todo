from django.views.generic import CreateView
from .models import ToDo
from .forms import TodoCreateForm


class TodoCreateView(CreateView):
    model = ToDo
    form_class = TodoCreateForm
    template_name = "todos/create.html"
