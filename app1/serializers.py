

from rest_framework import serializers
from .models import AccountManager, Song, Singer
from django.contrib.auth.models import User


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id','name','album_no','gender']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def profile(self, validated_data):
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
                user = user,
                first_name = profile_data['first_name'],
                last_name = profile_data['last_name'],
        )



#Adding up the User Profile
from .models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','first_name', 'id_created','image','contact_no']
        
        
        
    






