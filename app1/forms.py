from django import forms
from django.db import models
from .models import Singer, Song


class SingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        exclude=['']
        skip_unchanged = True

class SongForm(forms.ModelForm):
    class Meta:
        model = Song  
        exclude = ['']
        skip_unchanged = True
