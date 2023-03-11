from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomerUserCreationForm
from django.db import connection

from .models import Employee, ClientPurchase, Client

# Create your views here.
cursor = connection.cursor()


def index(requests):
    return render(requests, 'drauto/index.html')


def client_login(requests):
    # form = LoginForm()
    # context = {'form':form}
    page = 'login'

    if requests.user.is_authenticated:
        return redirect('/')

    if requests.method == 'POST':
        emp_name = requests.POST['username']
        password = requests.POST['password']

        user = authenticate(requests, username=emp_name, password=password)

        if user is not None:
            login(requests, user)
            return index(requests)
        else:
            print('Incorrect Credentials')
            messages.error(requests, 'Incorrect Credentials')

    return render(requests, 'drauto/login_register_form.html')


def login(requests):
    page = 'login'

    if requests.user.is_authenticated:
        return redirect('/')

    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']
        user_type = requests.POST.get('user_type')
        user = 'E'

        if user_type == 'staff':
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT dbo.ValidateLogin('{username}', '{password}', 'E')")
                result = cursor.fetchone()[0]
                if result == 1:
                    user = Employee.objects.create_user(emp_name=username, password=password)
        elif user_type == 'client':
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT dbo.ValidateLogin('{username}', '{password}', 'C')")
                result = cursor.fetchone()[0]
                if result == 1:
                    user = Client.objects.create_user(emp_name=username, password=password)
            #user = authenticate(requests, username=username, password=password)

        if user is not None:
            login(requests, user)
            return index(requests)
        else:
            print('Incorrect Credentials')
            messages.error(requests, 'Incorrect Credentials')
    return render(requests, 'drauto/login_register_form.html')
    #     if result == 1:
    #         user = Employee.objects.create_user(emp_name=username,password_hash=password)
    #         user = authenticate(requests, username=username, password_hash=password)
    #         user = requests.user
    #         login(requests, user)
    #         return index(requests)
    #     else:
    #         print('Incorrect Credentials')
    #         messages.error(requests, 'Incorrect Credentials')
    #
    # return render(requests, 'drauto/login_register_form.html')


def logout_user(requests):
    logout(requests)

    return redirect('/')


def register_form(requests):
    page = 'register'
    form = CustomerUserCreationForm(requests.POST or None)

    if requests.method == 'POST' and form.is_valid():
        client = form.save(commit=False)
        password = form.cleaned_data.get('password')
        client.set_password(password)
        client.save()

        # authenticate the user
        user = authenticate(email=client.email, password=password)
        if user is not None:
            # login the user
            login(requests, user)
            messages.success(requests, 'Your account has been created!')
            return redirect('home')
        else:
            messages.error(requests, "Unable to authenticate user")

    context = {'page': page, 'form': form}
    return render(requests, 'drauto/login_register_form.html', context)


def vehicle(requests):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM DrautoshopAddb.dbo.Vehicle")
        vehicle_list = cursor.fetchall()
        context = {
            'vehicle_list': vehicle_list,
        }

    return render(requests, 'drauto/vehicle.html', context)


def purchase(requests, vehicle_id):
    if not requests.user.is_authenticated:
        return redirect('/')

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM DrautoshopAddb.dbo.Vehicle")
        vehicle_list = cursor.fetchall()

        for v in vehicle_list:
            if v[0] == vehicle_id:
                # Store the values for the corresponding column names
                vehicle = {
                    'chassis_number': v[0],
                    'make': v[1],
                    'import_price_usd': v[2],
                    'car_year': v[3],
                    'markup_percent': v[4],
                    'colour': v[5],
                    'engine_number': v[6],
                    'model': v[7],
                    'car_type': v[8],
                    'condition': v[9],
                    'mileage': v[10],
                    'cc_rating': v[11],
                    'price': getPrice(v[0]),
                    'discount_price': getDiscountPrice(v[0]),
                }
                print(vehicle)
                break  # Exit the loop once the vehicle is found

        # If the vehicle is not found, set the purchase_id to 'Not Present'
        if not vehicle:
            vehicle = {'purchase_id': 'Not Present'}

    if requests.method == 'POST':
        form = ClientPurchase(requests.POST)
        if form.is_valid():
            purchase.amt_paid = form.cleaned_data['amt_paid']
            purchase.payment_method = form.cleaned_data['payment_method']

            # Save the purchase to the database
            purchase.save()

            return redirect('/')

        # If the form is not valid, render the purchase template with the form and vehicle information
    else:
        form = ClientPurchase()

    context = {'vehicle': vehicle}
    return render(requests, 'drauto/purchase.html', context)


def log_payment(requests):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO DrautoshopAddb.dbo.Client_Purchase ()")
        vehicle_list = cursor.fetchall()
        context = {
            'vehicle_list': vehicle_list,
        }


def getPrice(chassis_number):
    # cursor.execute("SELECT DrautoshopAddb.dbo.GET_VEHICLES_SELL_PRICE() WHERE chassis_number = '{chassis_number}'")
    cursor.execute(
        f"SELECT Selling_Price FROM DrautoshopAddb.dbo.GET_VEHICLE_SELL_PRICE() WHERE chassis_number = '{chassis_number}'")
    data = cursor.fetchall()

    return data[0][0]


def getDiscountPrice(chassis_number):
    cursor.execute("SELECT DrautoshopAddb.dbo.GET_DISCOUNT('{chassis_number}')")
    data = cursor.fetchall()

    return data[0][0]


def contact(requests):
    return render(requests, 'drauto/contact_page.html')


def stored_proc(requests, proc_string):
    cursor.execute('GET_VEHICLE_SELL_PRICE()')
    result = cursor.fetchall()
    return render(requests, '', {'result': result})
