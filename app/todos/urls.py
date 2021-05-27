from django.urls import path
from .views import TodoDetailView

app_name = "todos"


urlpatterns = [
    path("<int:pk>/", TodoDetailView.as_view(), name="detail"),
]