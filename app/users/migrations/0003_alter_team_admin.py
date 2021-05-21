# Generated by Django 3.2.3 on 2021-05-20 14:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_team_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='admin',
            field=models.ManyToManyField(related_name='admin_team', to=settings.AUTH_USER_MODEL),
        ),
    ]
