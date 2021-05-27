import os
import requests
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
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


def github_login(request):
    client_id = os.environ.get("GH_CLIENT_ID")
    redirect_uri = "http://0.0.0.0:8000/users/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri = {redirect_uri}&scope=read:user"
    )


class GithubException(Exception):
    pass


def github_callback(request):
    try:
        client_id = os.environ.get("GH_CLIENT_ID")
        client_secret = os.environ.get("GH_CLIENT_SECRET")
        code = request.GET.get("code", None)
        print(code)
        if code is not None:
            token = requests.post(
                f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                headers={"Accept": "application/json"},
            )
            token_json = token.json()
            error = token_json.get("error", None)
            if error is not None:
                raise GithubException("토큰 취득 중 에러가 발생하였습니다.")
            else:
                access_token = token_json.get("access_token")
                profile_request = requests.get(
                    "https://api.github.com/user",
                    headers={
                        "Authorization": f"token {access_token}",
                    },
                )
                profile_json = profile_request.json()
                username = profile_json.get("login", None)
                if username is not None:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    avatar_url = profile_json.get("avatar_url")
                    try:
                        user = User.objects.get(email=email)
                        if user.login_method != User.LOGIN_GITHUB:
                            raise GithubException(
                                f"깃허브 로그인이 아닌 다른 방법({user.login_method})으로 등록 된 유저입니다."
                            )
                    except User.DoesNotExist:
                        user = User.objects.create(
                            email=email,
                            name=name,
                            login_method=User.LOGIN_GITHUB,
                            social_avatar_url=avatar_url,
                            email_verified=True,
                        )
                        user.set_unusable_password()
                        user.save()
                    login(request, user)
                    return redirect(reverse("core:home"))
                else:
                    raise GithubException("프로필을 취득할 수 없습니다.")
        else:
            raise GithubException("코드를 취득하지 못하였습니다.")
    except GithubException:
        return redirect(reverse("users:login"))


def kakao_login(request):
    pass


def kakao_callback(request):
    pass
