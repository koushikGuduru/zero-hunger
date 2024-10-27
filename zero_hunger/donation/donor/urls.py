# donor/urls.py

from django.urls import path
from . import views

app_name = 'donor'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('donate/', views.donate, name='donate'),
    path('login/', views.donor_login, name='login')
]