from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout

from .models import Employee


# Create your views here.

def index(requests):
    return render(requests, 'drauto/index.html')


def login_form(requests):
    # form = LoginForm()
    # context = {'form':form}

    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']

        user = None
        try:
            user = authenticate(requests, username=username, password=password)
        except:
            print('User does not exists')

        if user is not None:
            login(requests, user)
            return redirect('drauto/index.html')
        else:
            print('Incorrect Credentials')

    return render(requests, 'drauto/login_form.html')


def logout_user(requests):
    logout(requests)
    return redirect('login_form')
