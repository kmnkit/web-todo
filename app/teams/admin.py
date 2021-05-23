from django.contrib import admin
from .models import Team


class MemberInlineAdmin(admin.TabularInline):
    model = Team.members.through


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Team Info",
            {
                "fields": ("name", "description"),
            },
        ),
    )
    inlines = (MemberInlineAdmin,)
