from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee
from .models import Client

class LoginForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['client_name','email','password1','password2']
        labels={
            'client_name': 'Name',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }