import random
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django_seed import Seed
from teams.models import Team, TeamMember
from faker import Faker

User = get_user_model()


class Command(BaseCommand):
    help = "샘플 유저 작성"

    def handle(self, *args, **options):
        users = User.objects.all()
        fake = Faker(locale="ko_KR")
        team_names = (
            "사업",
            "법무",
            "구매",
            "경영지원",
            "개발1",
            "개발2",
            "개발3",
            "디자인",
            "시장조사",
            "마케팅",
            "금융",
        )
        creating_list = [
            Team(name=name, description=fake.catch_phrase()) for name in team_names
        ]
        teams = Team.objects.bulk_create(creating_list)
        member_creating_list = []
        for team in teams:
            members = random.choices(users, k=10)
            for idx, member in enumerate(members):
                is_admin = False
                if idx == 0:
                    is_admin = True
                team_member = Team.members.through(
                    team=team, user=member, is_admin=is_admin
                )
                member_creating_list.append(team_member)
        Team.members.through.objects.bulk_create(member_creating_list)

        self.stdout.write(self.style.SUCCESS(f"{len(team_names)} teams created!"))