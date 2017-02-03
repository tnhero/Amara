from django import forms
from .models import User


class UserForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        Model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'address1']
