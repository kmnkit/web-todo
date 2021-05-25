from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.shortcuts import render, reverse, redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView
from .decorators import team_adminright_required
from .forms import CreateTeamForm, MemberJoinForm
from .models import Team, TeamMember

admin_rights = [login_required, team_adminright_required]


class TeamListView(ListView):
    model = Team
    template_name = "teams/list.html"
    context_object_name = "team_list"


class TeamCreateView(CreateView, LoginRequiredMixin):
    model = Team
    form_class = CreateTeamForm
    template_name = "teams/create.html"

    def form_valid(self, form):
        user = self.request.user
        team = form.save(commit=False)
        team.save()
        form.save_m2m()
        if user not in team.members.all():
            team.members.add(user)
        return redirect(reverse("teams:detail", args=(team.pk,)))


def team_detail_view(request, pk=None):
    team = Team.objects.get(pk=pk)
    member_list = team.team_members.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(member_list, 10, orphans=5)
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(
        request, "teams/detail.html", {"target_team": team, "members": members}
    )


@method_decorator(admin_rights, "get")
@method_decorator(admin_rights, "post")
class TeamDeleteView(DeleteView):
    model = Team
    template_name = "teams/delete.html"


class TeamMemberAddView(CreateView, LoginRequiredMixin):
    model = TeamMember
    template_name = "teams/add_member.html"


@login_required
def join_as_member(request, pk=None):
    if request.method == "POST":
        user = request.user
        team = Team.objects.get(pk=pk)
        form = MemberJoinForm(request.POST)
        if form.is_valid():
            nickname = form.data.get("nickname", None)
            if nickname is not None:
                Team.members.through.objects.create(
                    team=team, user=user, nickname=nickname
                )
                return redirect(reverse("teams:detail", kwargs={"pk": pk}))
        return redirect(reverse("teams:detail", kwargs={"pk": pk}))
