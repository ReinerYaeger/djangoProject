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
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM DrautoshopAddb.dbo.DrAuto_vehicle")
        vehicle_list = cursor.fetchall()
        context = {
            'vehicle_list': vehicle_list,
        }

    return render(requests, 'drauto/vehicle.html', context)


def purchase(requests, vehicle_id):

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM DrautoshopAddb.dbo.DrAuto_vehicle")
        vehicle_list = cursor.fetchall()

        for v in vehicle_list:
            if v[0] == vehicle_id:
                # Store the values for the corresponding column names
                vehicle = {
                    'purchase_id': v[0],
                    'client_Id': v[1],
                    'chassis_number': v[2],
                    'emp_Id': v[3],
                    'price': v[4],
                    'commission': v[5],
                    'date_sold': v[6],
                    'amt_paid': v[7],
                    'payment_method': v[8]
                }
                print(vehicle)
                break  # Exit the loop once the vehicle is found

        # If the vehicle is not found, set the purchase_id to 'Not Present'
        if not vehicle:
            vehicle = {'purchase_id': 'Not Present'}

    return render(requests, 'drauto/purchase.html',vehicle)


def contact(requests):
    return render(requests, 'drauto/contact_page.html')


def stored_proc(requests, proc_string):
    cursor.execute('')
    result = cursor.fetchall()
    return render(requests, '', {'result': result})
