from django.db import models


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


class Order(models.Model):
    order_name = models.CharField(max_length=30)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    # payment_id = models.ForeignKey(Payment, default=Null)

    
# Author Cashew <3
# Payment_Type Model blueprint design for database table
class Payment_Type(models.Model):
    name = models.CharField(max_length=30)
    account_num = models.IntegerField(unique=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True)



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