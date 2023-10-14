from django import forms
from .models import Comment , Favorite


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['post','name','email','subject','message']


class FovoriteForm(forms.ModelForm):
    class Mdta :
        model=Favorite
        fields='__all__'