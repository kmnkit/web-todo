from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

User = get_user_model()


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
    template_name = "users/detail.html"


class UserLeaveView(DeleteView, LoginRequiredMixin):
    model = User
    template_name = "users/leave.html"
    success_url = reverse_lazy("core:home")
