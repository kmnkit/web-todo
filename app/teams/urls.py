from django.urls import path
from .views import TeamCreateView, TeamDeleteView, team_detail_view, join_as_member

app_name = "teams"

urlpatterns = [
    path("create/", TeamCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", TeamDeleteView.as_view(), name="delete"),
    path("<int:pk>/", team_detail_view, name="detail"),
    path("<int:pk>/members/join/", join_as_member, name="member-join"),
]