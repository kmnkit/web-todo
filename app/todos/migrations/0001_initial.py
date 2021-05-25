# Generated by Django 3.2.3 on 2021-05-25 08:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0002_auto_20210523_1447'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.TextField(max_length=500)),
                ('importance', models.IntegerField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)], verbose_name='중요도')),
                ('is_finished', models.BooleanField(default=False)),
                ('assigned_member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='todos', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='teams.team')),
            ],
            options={
                'ordering': ['importance', 'assigned_member'],
            },
        ),
    ]
