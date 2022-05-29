# from cProfile import label
# from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core import validators
from django import forms
from .models import *

def checkalpha(value):
    # if value.startswith("," | "!" | "." | "/" | "<" | ">" | "{"):
        # raise forms.ValidationError("This is invalid")
    if value.isalpha() == False:
        raise forms.ValidationError('This is numeric')
        

class SignupForm(UserCreationForm):
    password2 = forms.CharField(label = 'Password Again', widget = forms.PasswordInput,
     error_messages= {'required':'This Password is required'})
    first_name = forms.CharField(widget = forms.TextInput,
     error_messages= {'required':'First Name is required'})
    last_name = forms.CharField(widget = forms.TextInput,
     error_messages= {'required':'Last Name is required'})
    email = forms.CharField(widget = forms.EmailInput,
     error_messages= {'required':'This Email is required'})
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        labels = {'username':"Enter Username",
                ' first_name':"Enter F-Name",
                    'last_name':"Enter L-Name" ,
                    'email':"Enter Email"}
                    
        widgets = {'username':forms.TextInput(attrs= {'class':'myclass'}),
                    'first_name':forms.TextInput(attrs= {'class':'myclass'}),
                    'last_name':forms.TextInput(attrs= {'class':'myclass'}),
                    'email':forms.EmailInput(attrs= {'class':'myclass'})}


        # error_messages = {'username':{'required':'This username is Required'},
        #                 'first_name':{'required':'This field is Required'},
        #                 'last_name':{'required':'This field is Required'},
        #                 'email':{'required':'This field is Required'}}


class Myreview(forms.Form):
    name = forms.CharField(validators=[checkalpha])
    subject = forms.CharField()
    review = forms.CharField(widget=forms.Textarea())
    hidden = forms.CharField(widget= forms.PasswordInput())
    tick = forms.BooleanField()   

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'username','password']


