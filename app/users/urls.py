from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserCreateView, UserDetailView

app_name = "users"

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="create"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("detail/<int:pk>/", UserDetailView.as_view(), name="detail"),
]