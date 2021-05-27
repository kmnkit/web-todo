from django.forms import ModelForm, ValidationError
from django.contrib.auth import get_user_model
from .models import ToDo
from teams.models import TeamMember

User = get_user_model()


class TodoCreateForm(ModelForm):
    class Meta:
        model = ToDo
        exclude = ["is_finished", "team"]

    def __init__(self, team, *args, **kwargs):
        super(TodoCreateForm, self).__init__(*args, **kwargs)
        self.team = team
        self.fields["assigned_member"].queryset = team.members.all()

    def clean_assignment(self):
        assignment = self.cleaned_data.get("assignment")
        if assignment == "":
            raise ValidationError("투두 내용을 반드시 입력하여야 합니다.")
        else:
            return assignment

    def clean_importance(self):
        importance = self.cleaned_data.get("importance")
        if importance < 1.0 or importance > 5.0:
            raise ValidationError("중요도는 1에서 5 사이여야 합니다.")
        else:
            return importance

    def clean_assigned_member(self):
        assigned_member = self.cleaned_data.get("assigned_member")
        if assigned_member is None:
            raise ValidationError("담당자를 반드시 배정하여야 합니다.")
        else:
            return assigned_member

    def save(self, *args, **kwargs):
        todo = super(TodoCreateForm, self).save(commit=False)
        assignment = self.cleaned_data.get("assignment")
        importance = self.cleaned_data.get("importance")
        assigned_member = self.cleaned_data.get("assigned_member")
        todo.team = self.team
        todo.assignment = assignment
        todo.importance = importance
        todo.asigned_member = assigned_member
        todo.save()
        return todo
