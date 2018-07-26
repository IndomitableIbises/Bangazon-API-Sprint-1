from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # type_id = models.ForeignKey(Product_Type)

# Authors Raf and Cashew <3
# Customer Model blueprint design for database table
class Customer(models.Model):
    account_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Product_Type(models.Model):
    name = models.CharField(max_length=30)


# Author Cashew <3
# Payment_Type Model blueprint design for database table
class Payment_Type(models.Model):
    name = models.CharField(max_length=30)
    account_num = models.IntegerField(unique=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
