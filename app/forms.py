from django import forms
from app.models import *


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        help_texts= {'username' : ''}


class AnimalsForm(forms.ModelForm):
    class Meta:
        model=Animals
        fields='__all__'