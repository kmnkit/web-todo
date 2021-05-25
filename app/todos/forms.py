from django.forms import ModelForm
from .models import ToDo


class TodoCreateForm(ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__"
