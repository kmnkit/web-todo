# Generated by Django 3.2.3 on 2021-05-27 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to=settings.AUTH_USER_MODEL, verbose_name='유저'),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(through='teams.TeamMember', to=settings.AUTH_USER_MODEL, verbose_name='팀 구성원'),
        ),
    ]
