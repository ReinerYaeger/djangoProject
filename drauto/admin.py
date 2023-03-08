from django.contrib import admin

# Register your models here.

from .models import Employee, Emergency_Contact, Salesman, Mechanic, Admin_Personnel, Supervisor, Vehicle, Car, Four_WD, Van, Client
from .models import Phone_Number,Client_Purchase,Emp_Purchase,Work_Done,Parts_Changed, Repair


admin.site.register(Employee)
admin.site.register(Emergency_Contact)
admin.site.register(Salesman)
admin.site.register(Mechanic)
admin.site.register(Admin_Personnel)
admin.site.register(Supervisor)
admin.site.register(Vehicle)
admin.site.register(Car)
admin.site.register(Four_WD)
admin.site.register(Van)
admin.site.register(Client)
admin.site.register(Phone_Number)
admin.site.register(Client_Purchase)
admin.site.register(Emp_Purchase)
admin.site.register(Work_Done)
admin.site.register(Parts_Changed)
admin.site.register(Repair)


