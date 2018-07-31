
from rest_framework import serializers
from API.models import Product, Customer, Product_Type, Payment_Type, Order, Employee, Training_Prog, Emp_Training, Department, Computer, Prod_Order


###########################################################################
# CUSTOMER SIDE SERIALIZERS
###########################################################################

# Authors Raf and Cashew <3
# Translates customer table database into json format
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'account_date', 'active', 'last_login', 'first_name', 'last_name')

# Authors: Cashew & Jake <3 - Prod_Order
class Prod_Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Prod_Order
        fields = '__all__'

# Authors: Sean & Jake - Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description', 'quantity', 'customer_id', 'type_id')

# Authors: Cashew, Jake, & Sean <3 - Prod_Order
class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'customer_id',  'payment_id', 'completed', 'products')

# Author Jake - Product_Type
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
# EMPLOYEE SIDE SERIALIZERS
###########################################################################

# Author Jake - Department
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'budget')

# Author Jake - Computer
class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ('id', 'purchase_date', 'decom_date')

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

# Author Raf - EmployeeSerializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' # this should automatically pipe in all field names and values once foreign keys in Employee Model are uncommented
