from django.forms import ModelForm
from .models import Profile,User, Logbook
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['course_of_interest', 'placement_addr', 'profile_image']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class LogForm(ModelForm):

    log_details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'type': 'text'}))
    class Meta:
        model = Logbook
        fields = ['week', 'day', 'log_details']




