from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee, ClientPurchase
from .models import Client


class LoginForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        db_table = 'auth_user'
        model = Client
        fields = ['client_name', 'email', 'residential_address']
        labels = {
            'client_name': 'Name',
            'email': 'Email Address',
            'residential_address': 'Home Address',
        }


class PaymentForm(forms.Form):
    PAYMENT_METHODS = (
        ('credit_card', 'Credit Card'),
        ('crypto_currency', 'Crypto Currency'),
        ('cash', 'Cash'),
    )
    payment_method = forms.ChoiceField(choices=PAYMENT_METHODS, widget=forms.RadioSelect)

    class Meta:
        model = ClientPurchase
        fields = ['amt_paid', 'payment_method']
        labels = {
            'amt_paid': 'Amount Paid',
            'payment_method': 'Payment Method',
        }
