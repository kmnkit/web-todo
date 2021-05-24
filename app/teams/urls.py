from django.urls import path
from .views import TeamCreateView, TeamDeleteView, team_detail_view

app_name = "teams"

urlpatterns = [
    path("create/", TeamCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", TeamDeleteView.as_view(), name="delete"),
    path("detail/<int:pk>/", team_detail_view, name="detail"),
]