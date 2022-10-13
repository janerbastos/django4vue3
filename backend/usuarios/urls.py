from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forgot-password', views.forgot_password, name="forgot-password"),
    path('recover-password', views.recover_password, name="recover-password"),
    path('changer-password', views.changer_password, name="changer-password"),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile')
]