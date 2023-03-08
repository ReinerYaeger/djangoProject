# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddOn(models.Model):
    work_done = models.OneToOneField('WorkDone', models.DO_NOTHING, primary_key=True)
    addon_description = models.CharField(db_column='addOn_description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Add_On'


class AdminPersonnel(models.Model):
    emp = models.OneToOneField('Employee', models.DO_NOTHING, db_column='emp_Id', primary_key=True)  # Field name made lowercase.
    salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Admin_Personnel'


class Car(models.Model):
    chassis_number = models.OneToOneField('Vehicle', models.DO_NOTHING, db_column='chassis_number', primary_key=True)
    seat_capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Car'


class Client(models.Model):
    client_id = models.CharField(db_column='client_Id', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    client_name = models.CharField(max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    email = models.CharField(max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    residential_address = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Client'


class ClientPurchase(models.Model):
    purchase_id = models.CharField(primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client_Id', blank=True, null=True)  # Field name made lowercase.
    chassis_number = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='chassis_number', blank=True, null=True)
    emp = models.ForeignKey('Employee', models.DO_NOTHING, db_column='emp_Id', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    date_sold = models.DateField(blank=True, null=True)
    amt_paid = models.FloatField(blank=True, null=True)
    payment_method = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Client_Purchase'


class DrautoAdminPersonnel(models.Model):
    emp_id = models.OneToOneField('DrautoEmployee', models.DO_NOTHING, db_column='emp_Id_id', primary_key=True)  # Field name made lowercase.
    salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DrAuto_admin_personnel'


class DrautoCar(models.Model):
    chassis_number = models.OneToOneField('DrautoVehicle', models.DO_NOTHING, primary_key=True)
    seat_capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DrAuto_car'


class DrautoClient(models.Model):
    client_id = models.CharField(db_column='client_Id', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    client_name = models.CharField(max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS')
    residential_address = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'DrAuto_client'


class DrautoClientPurchase(models.Model):
    purchase_id = models.CharField(primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    price = models.FloatField()
    commission = models.FloatField()
    date_sold = models.DateField()
    amt_paid = models.FloatField()
    payment_method = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    chassis_number = models.ForeignKey('DrautoVehicle', models.DO_NOTHING)
    client_id = models.ForeignKey(DrautoClient, models.DO_NOTHING, db_column='client_Id_id')  # Field name made lowercase.
    emp_id = models.ForeignKey('DrautoEmployee', models.DO_NOTHING, db_column='emp_Id_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrAuto_client_purchase'


class DrautoEmergencyContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    emergency_contact_number = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    emp_id = models.ForeignKey('DrautoEmployee', models.DO_NOTHING, db_column='emp_Id_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrAuto_emergency_contact'


class DrautoEmpPurchase(models.Model):
    purchase_id = models.CharField(primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    date_sold = models.DateField()
    vehicle_value = models.FloatField()
    price = models.FloatField()
    chassis_number = models.ForeignKey('DrautoVehicle', models.DO_NOTHING)
    emp_id = models.ForeignKey('DrautoEmployee', models.DO_NOTHING, db_column='emp_Id_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrAuto_emp_purchase'


class DrautoEmployee(models.Model):
    emp_id = models.CharField(db_column='emp_Id', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    emp_name = models.CharField(max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    date_employed = models.DateField()
    dob = models.DateField()
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DrAuto_employee'


class DrautoFourWd(models.Model):
    chassis_number = models.OneToOneField('DrautoVehicle', models.DO_NOTHING, primary_key=True)
    vehicle_size = models.FloatField()
    fuel_type = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'DrAuto_four_wd'


class DrautoMechanic(models.Model):
    emp_id = models.OneToOneField(DrautoEmployee, models.DO_NOTHING, db_column='emp_Id_id', primary_key=True)  # Field name made lowercase.
    salary = models.FloatField(blank=True, null=True)
    expertise = models.CharField(max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DrAuto_mechanic'


class DrautoPartsChanged(models.Model):
    id = models.BigAutoField(primary_key=True)
    part_name = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    part_description = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cost = models.FloatField()
    work_done = models.ForeignKey('DrautoWorkDone', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DrAuto_parts_changed'


class DrautoPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    client_id = models.OneToOneField(DrautoClient, models.DO_NOTHING, db_column='client_Id_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrAuto_phone_number'


class DrautoRepair(models.Model):
    id = models.BigAutoField(primary_key=True)
    repair_description = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cost = models.FloatField()
    work_done = models.ForeignKey('DrautoWorkDone', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DrAuto_repair'


class DrautoSalesman(models.Model):
    emp_id = models.OneToOneField(DrautoEmployee, models.DO_NOTHING, db_column='emp_Id_id', primary_key=True)  # Field name made lowercase.
    travel_subsistence = models.FloatField()

    class Meta:
        managed = False
        db_table = 'DrAuto_salesman'


class DrautoSupervisor(models.Model):
    emp_id = models.OneToOneField(DrautoEmployee, models.DO_NOTHING, db_column='emp_Id_id', primary_key=True)  # Field name made lowercase.
    date_assigned = models.DateField()

    class Meta:
        managed = False
        db_table = 'DrAuto_supervisor'


class DrautoVan(models.Model):
    chassis_number = models.OneToOneField('DrautoVehicle', models.DO_NOTHING, primary_key=True)
    haul_capacity = models.FloatField()
    max_clearance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'DrAuto_van'


class DrautoVehicle(models.Model):
    chassis_number = models.CharField(primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    make = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    import_price_usd = models.FloatField()
    car_year = models.DateField()
    markup_percent = models.FloatField()
    colour = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    engine_number = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    car_type = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    condition = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mileage = models.FloatField()
    cc_rating = models.CharField(max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'DrAuto_vehicle'


class DrautoWorkDone(models.Model):
    work_done_id = models.CharField(primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    hrs_worked = models.FloatField()
    emp_id = models.ForeignKey(DrautoEmployee, models.DO_NOTHING, db_column='emp_Id_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrAuto_work_done'


class EmergencyContact(models.Model):
    emergency_contact_number = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    emp = models.ForeignKey('Employee', models.DO_NOTHING, db_column='emp_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Emergency_Contact'


class EmpPurchase(models.Model):
    purchase_id = models.CharField(primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    chassis_number = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='chassis_number', blank=True, null=True)
    emp = models.ForeignKey('Employee', models.DO_NOTHING, db_column='emp_Id', blank=True, null=True)  # Field name made lowercase.
    date_sold = models.DateField(blank=True, null=True)
    vehicle_value = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emp_Purchase'


class Employee(models.Model):
    emp_id = models.CharField(db_column='emp_Id', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    emp_name = models.CharField(max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    date_employed = models.DateField()
    dob = models.DateField()

    class Meta:
        managed = False
        db_table = 'Employee'


class FourWd(models.Model):
    chassis_number = models.OneToOneField('Vehicle', models.DO_NOTHING, db_column='chassis_number', primary_key=True)
    vehicle_size = models.FloatField(blank=True, null=True)
    fuel_type = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Four_WD'


class Mechanic(models.Model):
    emp = models.OneToOneField(Employee, models.DO_NOTHING, db_column='emp_Id', primary_key=True)  # Field name made lowercase.
    salary = models.FloatField(blank=True, null=True)
    expertise = models.CharField(max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mechanic'


class PartsChanged(models.Model):
    work_done = models.OneToOneField('WorkDone', models.DO_NOTHING, primary_key=True)
    part_name = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    part_description = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Parts_Changed'


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    client = models.OneToOneField(Client, models.DO_NOTHING, db_column='client_Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Phone_Number'


class Repair(models.Model):
    work_done = models.OneToOneField('WorkDone', models.DO_NOTHING, primary_key=True)
    repair_description = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Repair'


class Salesman(models.Model):
    emp = models.OneToOneField(Employee, models.DO_NOTHING, db_column='emp_Id', primary_key=True)  # Field name made lowercase.
    travel_subsistence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Salesman'


class Supervisor(models.Model):
    emp = models.OneToOneField(Employee, models.DO_NOTHING, db_column='emp_Id', primary_key=True)  # Field name made lowercase.
    date_assigned = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Supervisor'


class Van(models.Model):
    chassis_number = models.OneToOneField('Vehicle', models.DO_NOTHING, db_column='chassis_number', primary_key=True)
    haul_capacity = models.FloatField(blank=True, null=True)
    max_clearance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Van'


class Vehicle(models.Model):
    chassis_number = models.CharField(primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    make = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    import_price_usd = models.FloatField(blank=True, null=True)
    car_year = models.DateField(blank=True, null=True)
    markup_percent = models.FloatField(blank=True, null=True)
    colour = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    engine_number = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    model = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    car_type = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    condition = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    mileage = models.FloatField(blank=True, null=True)
    cc_rating = models.CharField(max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vehicle'


class WorkDone(models.Model):
    work_done_id = models.CharField(primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    emp = models.ForeignKey(Employee, models.DO_NOTHING, db_column='emp_Id', blank=True, null=True)  # Field name made lowercase.
    hrs_worked = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Work_Done'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
