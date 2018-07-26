from django.db import models
# Authors Raf and Cashew <3


# Customer Model blueprint design for database table
class Customer(models.Model):
    account_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    # type_id = models.ForeignKey(Product_Type)

class Order(models.Model):
    order_name = models.CharField(max_length=30)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    # payment_id = models.ForeignKey(Payment, default=Null)


class Product_Type(models.Model):
    name = models.CharField(max_length=30)

