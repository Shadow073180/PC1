from django import forms
from .models import User, Pet, Match

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields =['id', 'first_name', 'last_name', 'picture', 'pet',]

class PetForm(forms.ModelForm):
    class Meta:
        model= Pet
        fields=['id', 'name']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields=['id', 'user']