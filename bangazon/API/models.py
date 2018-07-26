from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # type_id = models.ForeignKey(Product_Type)
