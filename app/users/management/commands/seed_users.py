from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker

User = get_user_model()


class Command(BaseCommand):
    help = "샘플 유저 작성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=10,
            type=int,
            help="얼마나 유저를 만들지",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        fake = Faker(locale="ko_KR")
        seeder.add_entity(
            User,
            number,
            {
                "avatar": None,
                "name": lambda x: fake.last_name() + fake.first_name(),
                "is_staff": False,
                "is_superuser": False,
                "social_avatar_url": None,
                "avatar": None,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))