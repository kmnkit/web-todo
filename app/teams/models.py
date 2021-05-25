from django.db import models
from .managers import CustomMemberManager


class Team(models.Model):
    name = models.CharField("이름", max_length=30, blank=False, null=False)
    description = models.TextField("팀 설명", max_length=255)
    members = models.ManyToManyField(
        "users.User",
        through="teams.TeamMember",
        verbose_name="팀 구성원",
    )

    class Meta:
        verbose_name = "팀"
        verbose_name_plural = "팀들"
        ordering = [
            "id",
        ]

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="team_members",
        verbose_name="유저",
    )
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_members", verbose_name="팀"
    )
    nickname = models.CharField("별명", max_length=50, null=True)
    is_admin = models.BooleanField(default=False, verbose_name="팀 관리자 여부")
    objects = CustomMemberManager()

    class Meta:
        verbose_name = "구성원"
        verbose_name_plural = "구성원들"
        ordering = ["team", "nickname"]

    def __str__(self):
        return f"{self.team} : {self.user.name}"
