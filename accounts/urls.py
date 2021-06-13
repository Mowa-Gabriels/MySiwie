from django.urls import path
from . import views

urlpatterns = [
 path('register/', views.register, name='register'),
 path('login/', views.login_user, name='login'),
 path('logout/', views.logout_user, name='logout'),
 path('validate_login/', views.login_validate, name='login_validate')

]