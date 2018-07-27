
from rest_framework import serializers
from API.models import Product, Customer, Product_Type, Payment_Type, Order, Employee, Training_Prog, Emp_Training


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description', 'quantity', 'customer_id', 'type_id')



# Authors Raf and Cashew <3
# Translates customer table database into json format
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'account_date', 'active', 'last_login', 'first_name', 'last_name')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'order_name', 'product_id', 'customer_id')


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


###########################################################################
# EMPLOYEE SIDE VIEWS
###########################################################################

# Author Raf - EmployeeSerializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' # this should automatically pipe in all field names and values once foreign keys in Employee Model are uncommented

# Authors: Cashew & Raf <3 - TrainingSerializer
class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training_Prog
        fields = '__all__'

# Authors: Cashew & Raf <3 - Emp_TrainSerializer
class Emp_TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp_Training
        fields = '__all__'