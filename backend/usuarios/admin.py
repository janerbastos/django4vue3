from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from .models import (
    User,
    UserProfile
)

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'username',
        'is_active',
        'last_login',
        'created_date'
    ]
    filter_horizontal = ()
    ordering = ['-date_joined']
    list_filter = []
    fieldsets = []

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)