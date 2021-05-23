from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserCreateView, UserDetailView

app_name = "users"

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail"),
]