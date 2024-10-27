from django.shortcuts import render

# Create your views here.


# receiver/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import ReceiverRegistrationForm, ReceiverProfileForm
from .models import Receiver

def register(request):
    if request.method == 'POST':
        user_form = ReceiverRegistrationForm(request.POST)
        profile_form = ReceiverProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            receiver = Receiver(user=user, phone_number=profile_form.cleaned_data['phone_number'])
            receiver.save()
            login(request, user)
            return redirect('receiver:home')
    else:
        user_form = ReceiverRegistrationForm()
        profile_form = ReceiverProfileForm()
    return render(request, 'receiver/register.html', {'user_form': user_form, 'profile_form': profile_form})

def home(request):
    return render(request, 'receiver/home.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def receiver_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('receiver:home')  # Redirect to receiver home
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'receiver/login.html')