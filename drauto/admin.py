from django.contrib import admin
from .models import Employee, EmergencyContact, Salesman, Mechanic, AdminPersonnel, Supervisor, Vehicle, Car, FourWD, Van, Client, PhoneNumber, ClientPurchase, EmpPurchase, WorkDone, PartsChanged, Repair, AddOn

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmergencyContact)
admin.site.register(Salesman)
admin.site.register(Mechanic)
admin.site.register(AdminPersonnel)
admin.site.register(Supervisor)
admin.site.register(Vehicle)
admin.site.register(Car)
admin.site.register(FourWD)
admin.site.register(Van)
admin.site.register(Client)
admin.site.register(PhoneNumber)
admin.site.register(ClientPurchase)
admin.site.register(EmpPurchase)
admin.site.register(WorkDone)
admin.site.register(PartsChanged)
admin.site.register(Repair)
admin.site.register(AddOn)
