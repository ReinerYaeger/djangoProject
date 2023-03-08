from django.db import models
from django.contrib.auth.models import Permission

# Create your models here.

class Employee(models.Model):
    emp_Id = models.CharField(max_length=10, primary_key=True)
    emp_name = models.CharField(max_length=25, null=False)
    date_employed = models.DateField(null=False)
    dob = models.DateField(null=False)
    age = models.IntegerField(null=True)


class Emergency_Contact(models.Model):
    emergency_contact_number = models.CharField(max_length=15)
    emp_Id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Salesman(models.Model):
    emp_Id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    travel_subsistence = models.FloatField()


class Mechanic(models.Model):
    emp_Id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    salary = models.FloatField(null=True)
    expertise = models.CharField(max_length=25, null=True)


class Admin_Personnel(models.Model):
    emp_Id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    salary = models.FloatField(null=True)


class Supervisor(models.Model):
    emp_Id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    date_assigned = models.DateField()


class Vehicle(models.Model):
    chassis_number = models.CharField(max_length=10, primary_key=True)
    make = models.CharField(max_length=20)
    import_price_usd = models.FloatField()
    car_year = models.DateField()
    markup_percent = models.FloatField()
    colour = models.CharField(max_length=15)
    engine_number = models.CharField(max_length=10)
    model = models.CharField(max_length=15)
    car_type = models.CharField(max_length=15)
    condition = models.CharField(max_length=10)
    mileage = models.FloatField()
    cc_rating = models.CharField(max_length=5)


class Car(models.Model):
    chassis_number = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    seat_capacity = models.IntegerField()


class Four_WD(models.Model):
    chassis_number = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    vehicle_size = models.FloatField()
    fuel_type = models.CharField(max_length=10)


class Van(models.Model):
    chassis_number = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    haul_capacity = models.FloatField()
    max_clearance = models.FloatField()


class Client(models.Model):
    client_Id = models.CharField(max_length=10, primary_key=True)
    client_name = models.CharField(max_length=25)
    email = models.CharField(max_length=35)
    residential_address = models.CharField(max_length=50)


class Phone_Number(models.Model):
    phone_number = models.CharField(max_length=15)
    client_Id = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)


class Client_Purchase(models.Model):
    purchase_id = models.CharField(max_length=10, primary_key=True)
    client_Id = models.ForeignKey(Client, on_delete=models.CASCADE)
    chassis_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    emp_Id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    price = models.FloatField()
    commission = models.FloatField()
    date_sold = models.DateField()
    amt_paid = models.FloatField()
    payment_method = models.CharField(max_length=15)


class Emp_Purchase(models.Model):
    purchase_id = models.CharField(max_length=10, primary_key=True)
    date_sold = models.DateField()
    vehicle_value = models.FloatField()
    price = models.FloatField()
    emp_Id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    chassis_number = models.ForeignKey('Vehicle', on_delete=models.CASCADE)


class Work_Done(models.Model):
    work_done_id = models.CharField(max_length=10, primary_key=True)
    hrs_worked = models.FloatField()
    emp_Id = models.ForeignKey('Employee', on_delete=models.CASCADE)


class Parts_Changed(models.Model):
    part_name = models.CharField(max_length=15)
    part_description = models.CharField(max_length=15)
    cost = models.FloatField()
    work_done = models.ForeignKey('Work_Done', on_delete=models.CASCADE)


class Repair(models.Model):
    repair_description = models.CharField(max_length=50)
    cost = models.FloatField()
    work_done = models.ForeignKey('Work_Done', on_delete=models.CASCADE)
