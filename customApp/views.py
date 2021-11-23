from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
#from rest_framework.authentication import IsAdminUser
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


@csrf_exempt
@api_view(['POST'])
#@authentication_classes([IsAdminUser])
@permission_classes([AllowAny])

def dashboard(request):
    profile = request.user
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response ({'BOT': 'Please provide the above credentials'},
                            status=HTTP_400_BAD_REQUEST)
    user = authenticate(username =username, password = password)
    if not User:
        return Response({'BOT': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                            status= HTTP_200_OK)        


@api_view(["POST",'GET'])
@permission_classes([AllowAny])
def Register_Users(request):
    try:
        data = {}
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            account.save()
            token = Token.objects.get_or_create(user=account)[0].key
          #  email = request.data.get("email")
           # password = request.data.get("password")
            data["email"] = account.email
            data["token"] = token
            data["username"] = account.email.split('@')[0]
            data["message"] = "user registered successfully"
        else:
            data = serializer.errors
        return Response(data)
    except IntegrityError as e:
        account=User.objects.get(username='')
        account.delete()
        raise ValidationError({"400": f'{str(e)}'})

    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


#now we will get the user data of out registered user