from django.urls import path
from .views import (
    TeamCreateView,
    TeamDeleteView,
    TeamDetailView,
    join_as_member,
)
from todos.views import create_todo

app_name = "teams"

urlpatterns = [
    path("create/", TeamCreateView.as_view(), name="create"),
    path("<int:pk>/", TeamDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", TeamDeleteView.as_view(), name="delete"),
    path("<int:pk>/members/join/", join_as_member, name="member-join"),
    path("<int:pk>/todos/create/", create_todo, name="create-todo"),
]