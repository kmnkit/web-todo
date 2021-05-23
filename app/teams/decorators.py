from django.http import HttpResponseForbidden
from .models import TeamMember


def team_adminright_required(func):
    def decorated(request, *args, **kwargs):
        member = TeamMember.objects.get(pk=kwargs["member_pk"])
        if member.is_admin is False:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
