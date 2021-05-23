from django.forms import ModelForm
from .models import Team


class CreateTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = "__all__"

    def save(self, *args, **kwargs):
        team = super().save(commit=False)
        return team
