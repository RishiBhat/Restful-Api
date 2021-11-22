from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#we will create a setup of the music website like spotify...


#The best place to create a user credentials is models.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.fields import EmailField




class Singer(models.Model):
    name = models.CharField(max_length=20)
    album_no = models.IntegerField()
    gender =  models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=25)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='SongBy')
    duration = models.IntegerField()

    def __str__(self):
        return self.title

#To register a superuser or any  other user we set up a custom User module, AbstractUser or AbstractBaseUser
#https://learndjango.com/tutorials/django-best-practices-referencing-user-model
from django.conf import Settings

class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an Email Id')
        user = self.model(
            Email_Address = self.normalize_email(email),
            username = self.normalize_email(email),
            )
        user.set_password(password)
        return user  
    
    def create_superuser(self, Email_Address, password):
        user = self.create_user(Email_Address=self.normalize_email(Email_Address), password=password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

# class Users(AbstractBaseUser):
#     Email_Address = models.EmailField(verbose_name="email", max_length=20, unique=True, blank=True, null=True, default=None)
#     name = models.CharField(max_length=30, blank=True, null=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_teacher = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_super_teacher = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
    
#     USERNAME_FIELD = 'Email_Address'

#     class Meta:
#         db_table = "tbl_users"
        
#     def __str__(self):
#         return str(self.email)


#     def has_perm(self, perm, obj=None): return self.is_superuser

#     def has_module_perms(self, app_label): return self.is_superuser
    
#     objects = AccountManager()

#-------------------------------------------------Now we will implement the User Profile using the one-to-one relation
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICES = (
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Supervisor', 'Supervisor'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="",blank=True,null=True)
    location = models.CharField(max_length=30, blank=True, default="")
    birthdate = models.DateField(null=True, blank=True,default=0)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


    # def profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    # post_save.connect(profile, sender=User)


# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

