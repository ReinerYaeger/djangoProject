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
        db_table = 'client'
        model = Client
        fields = ['client_name', 'email', 'password1']
        labels = {
            'client_name': 'Name',
            'email': 'Email Address',
            'password1': 'Password',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Client.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
