from django.urls import path
from .views import TodoCreateView

app_name = "todos"


urlpatterns = [
    path("create/", TodoCreateView.as_view(), name="create"),
]