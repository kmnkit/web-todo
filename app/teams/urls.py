from django.urls import path
from .views import TeamCreateView, TeamDetailView, TeamDeleteView

app_name = "teams"

urlpatterns = [
    path("create/", TeamCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", TeamDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", TeamDeleteView.as_view(), name="delete"),
]