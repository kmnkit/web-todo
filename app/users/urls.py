from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    UserCreateView,
    UserDetailView,
    github_login,
    github_callback,
    kakao_login,
    kakao_callback,
)

app_name = "users"

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("login/github/", github_login, name="github-login"),
    path("login/github/callback/", github_callback, name="github-callback"),
    path("login/kakao/", kakao_login, name="kakao-login"),
    path("login/kakao/callback/", kakao_callback, name="kakao-callback"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail"),
]