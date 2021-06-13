from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(State)
admin.site.register(Internship)
admin.site.register(Week)
admin.site.register(Day)
admin.site.register(Logbook)

