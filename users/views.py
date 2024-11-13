from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from.utils import send_welcome_email
from .forms import UserSignUpForm
from django.contrib.auth import authenticate, login, logout
from .utils import convert_timezone
# Create your views here.


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            un = form.cleaned_data.get('username') # pylint: disable=invalid-name
            messages.success(request, f'Account created for {un}.')
            send_welcome_email(form.cleaned_data.get('email'))
            return redirect('sign_in')

    elif request.method == "GET":
        form = UserSignUpForm()
    
    return render(request, 'users/signup.html', {'form': form})


#RAPID API
