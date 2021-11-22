from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Singer, Song

@admin.register(Singer)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','album_no']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id','title','singer','duration']
     


# @admin.register(Users)
# class UsersAdmin(admin.ModelAdmin):
#      search_fields = ['Email_Address','name','is_admin','is_active','is_teacher','is_staff','is_super_teacher','is_superuser']



     #here we are searching about the values which we get fromm the user.. so we have to use the search_fields option 

#Now We will extend the default UserAdmin, add the profile instance as an inline and switch the UserAdmin Django uses.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

#Admin Interface has the ability to edit models on the same page as a parent model. These are c/d inlines. 


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
 