from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """유저 모델. 이메일을 유저네임 대신 사용"""

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )
    avatar = models.ImageField(upload_to="users/avatar/", null=True)
    social_avatar_url = models.URLField(max_length=255, null=True, default=None)
    email = models.EmailField("이메일", max_length=255, unique=True)
    name = models.CharField("이름", max_length=255)
    is_active = models.BooleanField("활성화 여부", default=True)
    is_staff = models.BooleanField("스탭 여부", default=False)
    login_method = models.CharField(
        "로그인 방법", choices=LOGIN_CHOICES, max_length=20, default=LOGIN_EMAIL
    )
    email_verified = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = "유저들"
        ordering = [
            "pk",
        ]
