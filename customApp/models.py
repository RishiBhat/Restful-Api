from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.signals import post_save
from django.dispatch import receiver

PERMISSION_CLASSES = (
    ('Admin', 'Admin'),
    ('Editor', 'Editor'),
    ('Person', 'Person'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="", null= True, blank=True)
    location = models.CharField(max_length=10)
    phone_no = models.IntegerField()
    image = models.ImageField(upload_to="images",blank= True, null=True)
    hierarchy = models.CharField( default="",max_length=50,choices=PERMISSION_CLASSES, null=True, blank=True)
    
    def __str__(self):
        return self.user.username







