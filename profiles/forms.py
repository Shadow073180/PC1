from django import forms
from .models import User, Pet, Match

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields =['id', 'first_name', 'last_name', 'picture', 'pet']