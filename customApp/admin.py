from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import ProtectedError
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name')
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)