from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddCommentForm(forms.ModelForm):
    text = forms.CharField(label='Comment', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = Comments
        fields = ['text', ]
