# receiver/urls.py

from django.urls import path
from . import views

app_name = 'receiver'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/', views.receiver_login, name='login'),
]