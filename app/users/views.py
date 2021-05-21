from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView
from .decorators import team_adminright_required
from .models import Team

User = get_user_model()
has_ownership = [team_adminright_required, login_required]


class TeamCreateView(CreateView, LoginRequiredMixin):
    model = Team
    template_name = "users/team_create.html"


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class TeamDeleteView(DeleteView):
    model = Team


class UserCreateView(CreateView):
    """ 회원가입 뷰 """

    model = User
    form_class = UserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("users:detail")


class UserDetailView(DetailView):
    """ 회원 정보 뷰 """

    model = User
    context_object_name = "user_obj"


class UserLeaveView(DeleteView):
    model = User
    template_name = "users/leave.html"
    success_url = reverse_lazy("core:home")
