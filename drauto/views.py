from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Employee


# Create your views here.

def index(requests):
    return render(requests, 'drauto/index.html')


def login_form(requests):
    # form = LoginForm()
    # context = {'form':form}

    if requests.user.is_authenticated:
        return index(requests)


    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']

        user = authenticate(requests, username=username, password=password)

        if user is not None:
            login(requests, user)
            return index(requests)
        else:
            print('Incorrect Credentials')
            messages.error(requests, 'Incorrect Credentials')

    return render(requests, 'drauto/login_form.html')


def logout_user(requests):
    logout(requests)

    return redirect('login_form')
