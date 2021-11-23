from django.contrib.auth.admin import UserAdmin
from rest_framework import serializers
from customApp.models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =  ['user','location','phone_no','image']


from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
    
    def profile(self, validated_data):
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
                user = UserAdmin,
                first_name = profile_data['first_name'],
                last_name = profile_data['last_name'],
        )


