from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView

urlpatterns = [
 path('register/', views.register, name='register'),
 path('login/', views.login_user, name='login'),
 path('logout/', views.logout_user, name='logout'),
 path('validate_login/', views.login_validate, name='login_validate'),
 path('password_cHAnGe/', PasswordsChangeView.as_view(), name='password_change'),

]