# Generated by Django 3.2.3 on 2021-05-20 14:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='admin',
            field=models.ManyToManyField(null=True, related_name='admin_team', to=settings.AUTH_USER_MODEL),
        ),
    ]
