from django.urls import path
from teams.views import TeamListView

app_name = "core"

urlpatterns = [
    path("", TeamListView.as_view(), name="home"),
]
