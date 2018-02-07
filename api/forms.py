from django import forms
from .models import Create
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout)

class RegistForm(forms.Form):
    #EmpId = forms.AutoField(primary_key=True)
    EmpName = forms.CharField(required=True)
    Address = forms.CharField(required=True)
    EmailId = forms.EmailField(required=True)
    Password = forms.CharField(required=True,widget=forms.PasswordInput)
    Phone = forms.CharField(required=True)
    Image = forms.ImageField()


    


class Login(forms.Form):
    EmailId = forms.EmailField(required=True)
    Password = forms.CharField(required=True)




