
from rest_framework import serializers
from API.models import Product, Customer, Product_Type, Payment_Type, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description', 'quantity')



# Authors Raf and Cashew <3
# Translates customer table database into json format
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'account_date', 'active', 'last_login', 'first_name', 'last_name')

        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'order_name')


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Type
        fields = ('id', 'name')

# Author Cashew <3
# Translates customer table database into json format
class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Type
        fields = ('id', 'name', 'account_num', 'customer_id')