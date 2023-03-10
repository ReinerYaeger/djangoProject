from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import Permission, AbstractUser


class Employee(AbstractBaseUser):
    emp_Id = models.CharField(max_length=10, primary_key=True)
    emp_name = models.CharField(max_length=25)
    date_employed = models.DateField()
    dob = models.DateField()
    age = models.IntegerField(null=True)

    class Meta:
        db_table = "Employee"


class EmergencyContact(models.Model):
    emergency_contact_number = models.CharField(max_length=15)
    emp_Id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        db_table = "Emergency_Contact"


class Salesman(models.Model):
    emp_Id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    travel_subsistence = models.FloatField()

    class Meta:
        db_table = "Salesman"


class Mechanic(models.Model):
    emp_Id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    salary = models.FloatField(null=True)
    expertise = models.CharField(max_length=25, null=True)

    class Meta:
        db_table = "Mechanic"


class AdminPersonnel(models.Model):
    emp_Id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    salary = models.FloatField(null=True)

    class Meta:
        db_table = "Admin_Personnel"


class Supervisor(models.Model):
    emp_Id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    date_assigned = models.DateField()

    class Meta:
        db_table = "Supervisor"


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

    class Meta:
        db_table = "Vehicle"


class Car(models.Model):
    chassis_number = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    seat_capacity = models.IntegerField()

    class Meta:
        db_table = "Car"


class FourWD(models.Model):
    chassis_number = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    vehicle_size = models.FloatField()
    fuel_type = models.CharField(max_length=10)

    class Meta:
        db_table = "Four_WD"


class Van(models.Model):
    chassis_number = models.OneToOneField(Vehicle, on_delete=models.CASCADE, primary_key=True)
    haul_capacity = models.FloatField()
    max_clearance = models.FloatField()

    class Meta:
        db_table = "Van"


class ClientManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser):
    client_Id = models.CharField(max_length=10, primary_key=True)
    client_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=35)
    residential_address = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'

    objects = ClientManager()

    class Meta:
        db_table = "client"


class PhoneNumber(models.Model):
    client_Id = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=15)

    class Meta:
        db_table = "Phone_Number"


from django.db import models


class ClientPurchase(models.Model):
    purchase_id = models.CharField(max_length=10, primary_key=True)
    client_id = models.CharField(max_length=10)
    chassis_number = models.CharField(max_length=10)
    emp_id = models.CharField(max_length=10)
    price = models.FloatField()
    commission = models.FloatField()
    date_sold = models.DateField()
    amt_paid = models.FloatField()
    payment_method = models.CharField(max_length=15)

    class Meta:
        db_table = 'Client_Purchase'


class EmpPurchase(models.Model):
    purchase_id = models.CharField(max_length=10, primary_key=True)
    chassis_number = models.CharField(max_length=10)
    emp_id = models.CharField(max_length=10)
    date_sold = models.DateField()
    vehicle_value = models.FloatField()
    price = models.FloatField()

    class Meta:
        db_table = 'Emp_Purchase'


class WorkDone(models.Model):
    work_done_id = models.CharField(max_length=10, primary_key=True)
    emp_id = models.CharField(max_length=10)
    hrs_worked = models.FloatField()

    class Meta:
        db_table = 'Work_Done'


class PartsChanged(models.Model):
    work_done_id = models.CharField(max_length=10, primary_key=True)
    part_name = models.CharField(max_length=15)
    part_description = models.CharField(max_length=15)
    cost = models.FloatField()

    class Meta:
        db_table = 'Parts_Changed'


class Repair(models.Model):
    work_done_id = models.CharField(max_length=10, primary_key=True)
    repair_description = models.CharField(max_length=50)
    cost = models.FloatField()

    class Meta:
        db_table = 'Repair'


class AddOn(models.Model):
    work_done_id = models.CharField(max_length=10, primary_key=True)
    addOn_description = models.CharField(max_length=50)
    cost = models.FloatField()

    class Meta:
        db_table = 'Add_On'
