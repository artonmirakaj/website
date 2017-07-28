from django.contrib.auth.models import User
#base user class
from django import forms


class UserForm(forms.ModelForm):
    #blueprint for making forms
    password = forms.CharField(widget=forms.PasswordInput)

    # information about your class
    class Meta:
        model = User
        #when user signs up for site
        fields = ['username', 'email', 'password']