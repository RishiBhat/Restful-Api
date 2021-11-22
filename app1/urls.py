from django.conf import settings
from django.urls import path, include  
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter
#from rest_framework.authtoken.views import obtain_auth_token

#now using the custom auth file to call the api for the token and take the id and credentials
from app1.auth import CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token
from core.settings import STATIC_URL

urlpatterns = [    

    path('dashboard',views.dashboard, name="dashboard"),
    path('registrations',views.Register_Users, name="Register_Users"),
    #giving the url for getting the token by expsoing the endpoint
    path('gettoken/',CustomAuthToken.as_view()), 
    path('login', obtain_auth_token, name = 'login' )

]


