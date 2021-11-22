#from typing_extensions import Self

# Create your views here.

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
#for the function base view we have to apply it here

#now we will start calling our api from the function based view



#Reference Blog:- https://medium.com/quick-code/token-based-authentication-for-django-rest-framework-44586a9a56fb

from rest_framework.response import Response
from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer, RegistrationSerializer
from .forms import SingerForm, SongForm
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User 
#from django.contrib.auth.User import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


@csrf_exempt
@api_view(['POST'])
#@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([AllowAny])

def dashboard(request):
    #profile = request.user
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
@api_view(["POST"])
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
            data["message"] = "user registered successfully"
            data["email"] = account.email
            data["username"] = account.username
            data["token"] = token

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








      #  serializer = SingerSerializer(data=request.data)
       # data = {}
       # if serializer.is_valid():
       #     account = serializer.save()
        #    username = serializer.cleaned_data.get("username")
        ##   data['response'] = "Successfullly Registered"
          #  data['email'] = account.email
          #  data ['username'] = account.username
           # token = Token.objects.get(user=request.user)
           # data['token'] = token
        #else:
        #    data = serializer.errors
      #  return Response(data)
        
     #   if profile.is_valid():
      #      username = profile.cleaned_data.get("username")
       #     password = profile.cleaned_data.get("password")
        #    user = authenticate(username=username, password=password)
            #if user is not None:
            #    toke = 
           # else:    
            #    msg = 'Invalid credentials'    
       # else:
        #    msg = 'Error validating the form'    
    #return render(request, "accounts/login.html", {"form": profile, "msg" : user})#

#-----------------This will be the class based view will be creating just for our understanding--------------------

#class ExampleView(APIView):
 #   authentication_classes = [SessionAuthentication, BasicAuthentication]
 #   permission_classes = [IsAuthenticated]

    #def get(self, request, format = None):
    #    content = {
     #       'user': unicode(request.user)
      #      'auth': unicode(request.auth)
       # }
        #return Response(content)