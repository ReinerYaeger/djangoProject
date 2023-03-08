from django.forms import ModelForm
from .models import Employee

class LoginForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'