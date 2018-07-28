from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


###########################################################################
# CUSTOMER SIDE DATABASE
###########################################################################
# Authors Raf and Cashew <3
# Customer Model blueprint design for database table
class Customer(models.Model):
    account_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    ## Shows in field when you grab the foreign key the f/l name of the customer
    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

class Product_Type(models.Model):
    name = models.CharField(max_length=30)

    ## Shows in field when you grab the foreign key the name of the product type
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    type_id = models.ForeignKey(Product_Type, on_delete=models.CASCADE, null=True, blank=True)

    ## Shows in field when you grab the foreign key the title of the product
    def __str__(self):
        return "{0}".format(self.title)

# Author Cashew <3
# Payment_Type Model blueprint design for database table
class Payment_Type(models.Model):
    name = models.CharField(max_length=30)
    account_num = models.IntegerField(unique=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True)

class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    payment_id = models.ForeignKey(Payment_Type, on_delete=models.CASCADE, blank=True, null=True, default=None)

    



###########################################################################
# EMPLOYEE SIDE DATABASE
###########################################################################

# Author Raf - Employee Model
class Employee(models.Model):
    # training_id = models.ForeignKey('Training', on_delete=models, CASCADE, null=True, blank=True)
    # department_id = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    # computer_id = models.ForeignKey('Computer', on_delete=models.CASCADE, null=True, blank=True)
    supervisor = models.BooleanField(default=False)
    name = models.CharField(max_length=30)

    ## Shows in field when you grab the foreign key the name of the employee
    def __str__(self):
        return f'{self.name}'

# Authors: Cashew & Raf <3 - Training_Prog
class Training_Prog(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_attendees = models.PositiveIntegerField() # We need to find away to set the range from 1-100 and possibly allow a user to create an event and manually set the max attendees number

    def __str__(self):
        return f'{self.name}'

# Authors: Cashew & Raf <3 - Emp_Training
class Emp_Training(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.PROTECT, null=True, blank=True)
    training_id = models.ForeignKey('Training_Prog', on_delete=models.PROTECT, null=True, blank=True)
