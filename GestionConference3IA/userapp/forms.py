from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'affiliation', 'nationality']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Entrez votre email universitaire'}),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
     
        }