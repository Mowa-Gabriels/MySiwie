from django import forms
from siwieapp.models import User, Profile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
    password1 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',

        ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class ProfileForm(ModelForm):


    class Meta:
        model = Profile
        fields = ['course_of_interest']
        widgets ={
            'course_of_interest': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'col': 20})
        }

