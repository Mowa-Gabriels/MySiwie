from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver




class User(AbstractBaseUser, PermissionsMixin):
    '''This model spells out the authorization requirements'''


    username = models.CharField(_('Username'), max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_user = models.BooleanField(_('user'), default=True)
    is_admin = models.BooleanField(_('admin'), default=False)
    is_staff = models.BooleanField(_('staff'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)




class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_of_interest = models.CharField(max_length=225, blank=True)
    phone_no = models.CharField(max_length=14, blank=True)
    placement_addr = models.CharField(max_length=225, blank=True)
    profile_image = models.ImageField(default='he.png', upload_to='user/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   instance.profile.save()

class State(models.Model):
    name = models.CharField(max_length=224)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=224)

    def __str__(self):
        return self.name
    
class Internship(models.Model):
    PAY = (
        ('Yes', 'yes'),
        ('No', 'no'),
        ('Maybe', 'maybe'),
    )

    name_of_org = models.CharField(max_length=224)
    address = models.CharField(max_length=224)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tel = models.CharField(max_length=224)
    pay_status = models.CharField(max_length=14, null=True, choices=PAY)


    def __str__(self):
        return self.name_of_org


class Week(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Day(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Logbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    log_details = models.CharField(max_length=224)
    date_posted = models.DateTimeField(auto_now_add=True)
    # log_image = models.ImageField(default='default-avatar.png', upload_to='user/', null=True, blank=True)

    def __str__(self):
        return "Week{} - Day{}".format(self.week.name[:25], self.day.name[:25])

