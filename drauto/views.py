from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerUserCreationForm
from django.db import connection

from .models import Employee

# Create your views here.
cursor = connection.cursor()


def index(requests):
    return render(requests, 'drauto/index.html')


def login_form(requests):
    # form = LoginForm()
    # context = {'form':form}
    page = 'login'

    if requests.user.is_authenticated:
        return redirect('/')

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

    return render(requests, 'drauto/login_register_form.html')


def logout_user(requests):
    logout(requests)

    return redirect('/')


def register_form(requests):
    page = 'register'
    form = CustomerUserCreationForm()
    context = {'page': page, 'form': form}

    if requests.method == 'POST':
        form = CustomerUserCreationForm(requests.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(requests.POST['password'])
            user.save()

            messages.success(requests, "User created")
            login(requests, user)
        else:
            messages.error(requests, "An error has occurred during registration")

    return render(requests, 'drauto/login_register_form.html', context)


def vehicle(requests):

    return render(requests, 'drauto/vehicle.html')


def contact(requests):
    return render(requests, 'drauto/contact_page.html')


def stored_proc(requests, proc_string):
    cursor.execute('')
    result = cursor.fetchall()
    return render(requests, '', {'result': result})
