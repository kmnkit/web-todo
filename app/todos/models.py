from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ToDo(models.Model):
    assignment = models.TextField(max_length=500, null=False)
    team = models.ForeignKey(
        "teams.Team", related_name="todos", on_delete=models.CASCADE
    )
    assigned_member = models.ForeignKey(
        "users.User",
        related_name="todos",
        on_delete=models.SET_NULL,
        null=True,
    )
    importance = models.IntegerField(
        "중요도", validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )
    is_finished = models.BooleanField(default=False)

    class Meta:
        ordering = ["importance", "assigned_member"]

    def __str__(self):
        return self.assignment
