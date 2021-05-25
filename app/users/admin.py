from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ("id",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "avatar", "social_avatar_url")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "login_method")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    list_filter = UserAdmin.list_filter

    list_display = ("name", "email")
