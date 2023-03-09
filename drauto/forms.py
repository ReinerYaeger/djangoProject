from django.core.exceptions import ValidationError
from django.forms import ModelForm, forms
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
        db_table = 'auth_user'
        model = Client
        fields = ['client_name', 'email']
        labels = {
            'client_name': 'Name',
            'email': 'Email Address'
        }
