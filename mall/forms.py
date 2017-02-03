from django import forms
from .models import User


class UserForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'telephone', 'address1']
