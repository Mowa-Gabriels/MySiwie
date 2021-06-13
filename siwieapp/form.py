from django.forms import ModelForm
from .models import Profile,User, Logbook


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['course_of_interest', 'placement_addr', 'profile_image']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class LogForm(ModelForm):
    class Meta:
        model = Logbook
        fields = ['week', 'day', 'log_details']

