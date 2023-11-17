from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class AdminUser(UserAdmin):
    model = User

    list_display = ('mail', 'username', 'first_name', 'last_name')
    search_fields = ('mail', 'first_name', 'last_name')
    list_filter = ('username', 'email')
