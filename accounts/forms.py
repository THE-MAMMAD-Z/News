# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=False)
    profile_photo = forms.ImageField(required=False)
    Gender = forms.ChoiceField(choices=CustomUser.status_choices, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'full_name', 'phone_number', 'profile_photo', 'Gender', 'address', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=False)
    profile_photo = forms.ImageField(required=False)
    Gender = forms.ChoiceField(choices=CustomUser.status_choices, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'full_name', 'phone_number', 'profile_photo', 'Gender', 'address']
