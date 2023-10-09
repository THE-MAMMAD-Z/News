from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserChangeForm


class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username= forms.CharField( max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email= forms.EmailField(widget=forms.EmailInput)
    
    class Meta:
        model = UserProfile
        fields=['profile_picture','phone','Gender','address']
    


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['profile_picture','Gender','phone','address']


class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields=['first_name','last_name','email']
    password=None




# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('profile_picture', 'first_name', 'last_name', 'email', 'phone')