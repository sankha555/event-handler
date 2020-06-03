from django import forms 
from users.models import Creator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreatorRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CreatorProfileForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ['first_name', 'last_name', 'gmail_email', 'image']

