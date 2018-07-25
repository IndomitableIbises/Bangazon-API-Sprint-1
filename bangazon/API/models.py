from django.db import models


# Create your models here.

# Customer Model
class Customer(models.Model):
    account_date = models.DateTimeField(auto_now_add=True)
    active_inactive = models.BooleanField(default=True)
    last_login = models.DateTimeField('{account_date}')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)