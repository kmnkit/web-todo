from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden
from .models import Team

User = get_user_model()


def team_adminright_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs["user_pk"])
        team = (
            Team.objects.select_related("admin").filter(pk=kwargs["team_pk"]).only("pk")
        )
        if user not in team:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
