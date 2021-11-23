from django.conf import settings
from django.urls import path, include  
from django.contrib import admin
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from UserProfileToken.settings import STATIC_URL

urlpatterns = [    
    path('dashboard',views.dashboard, name="dashboard"),
    path('registrations',views.Register_Users, name="Register_Users"),
     
    
]
