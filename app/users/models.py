from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class Team(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    admin = models.ManyToManyField(
        "users.User",
        related_name="admin_team",
    )

    def __str__(self):
        return self.name


class User(AbstractUser):
    """유저 모델. 이메일을 유저네임 대신 사용"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    team = models.ForeignKey(
        "Team", on_delete=models.SET_NULL, null=True, related_name="members"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
    ]

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = [
            "date_joined",
        ]
