from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser #, Profile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username','email','date_joined']

admin.site.register(CustomUser, CustomUserAdmin)

#admin.site.register(Profile)