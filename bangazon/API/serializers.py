
from rest_framework import serializers
from API.models import Product, Customer, Department
from API.models import Product, Customer, Product_Type, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'account_date', 'active', 'last_login', 'first_name', 'last_name')



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'order_name')


# 'customer_id', 'type_id'

# Authors Raf and Cashew <3

# Translates database into json format

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'budget')

        # 'supervisor_id'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Type
        fields = ('id', 'name')
