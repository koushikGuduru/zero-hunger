# donor/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import DonorRegistrationForm, DonorProfileForm
from .models import Donor,Donation

def register(request):
    if request.method == 'POST':
        user_form = DonorRegistrationForm(request.POST)
        profile_form = DonorProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            donor = Donor(user=user, phone_number=profile_form.cleaned_data['phone_number'])
            donor.save()
            login(request, user)
            return redirect('donor:donate')
    else:
        user_form = DonorRegistrationForm()
        profile_form = DonorProfileForm()
    return render(request, 'donor/register.html', {'user_form': user_form, 'profile_form': profile_form})

def donate(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        donation = Donation(donor=request.user.donor, item=item)
        donation.save()
        return redirect('donor:donate')
    return render(request, 'donor/donate.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def donor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('donor:home')  # Redirect to donor home
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'donor/login.html')