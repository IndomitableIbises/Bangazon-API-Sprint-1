# Authors Raf and Cashew <3

from django.db import models


# Customer Model blueprint design for database table
class Customer(models.Model):
    account_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)