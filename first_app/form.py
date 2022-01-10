from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.db.models import fields
from first_app.models import *
from django.contrib.auth.models import User as authUser

class UserForm(forms.Form): 
    name = forms.CharField(label='Your name ', max_length=100)
    email = forms.EmailField(label='Your email ')
    text = forms.CharField(widget=forms.Textarea)
    hidden_input = forms.CharField(required=False, widget=forms.HiddenInput)

    # def clean_hidden_input(self): 
    #     hidden_input = self.cleaned_data['hidden_input']

    #     if len(hidden_input) > 0 :
    #         msg = 'bot detected!'
    #         print(msg)
    #         raise ValidationError(msg)
    #     return hidden_input

    # def clean_name(self): 
    #     name = self.cleaned_data['name']

    #     if str(name) == '123': 

    #         raise ValidationError('123')
    #     return name

class UserModelForm(forms.ModelForm): 
    password = forms.fields.CharField(label='Your password', widget=forms.PasswordInput())

    class Meta: 
        model = authUser
        fields = ['username', 'email', 'password']

class UserProfileInfoForm(forms.ModelForm): 
    profolio = forms.fields.URLField(required=False)
    picture = forms.fields.ImageField(required=False)

    class Meta: 
        model = UserProfileInfo
        exclude = (['user'])

class LoginForm(forms.Form): 
    username = forms.fields.CharField(label='username')
    password = forms.fields.CharField(label='password', widget=forms.PasswordInput())