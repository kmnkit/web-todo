from django.forms import ModelForm
from .models import Team, TeamMember


class CreateTeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = "__all__"

    def save(self, *args, **kwargs):
        team = super().save(commit=False)
        return team


class MemberJoinForm(ModelForm):
    class Meta:
        model = TeamMember
        fields = ("nickname",)
