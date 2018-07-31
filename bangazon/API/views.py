
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from API.models import Product, Product_Type, Customer, Order, Payment_Type, Employee, Training_Prog, Emp_Training, Department, Computer, Prod_Order
from API.serializers import ProductSerializer, ProductTypeSerializer, CustomerSerializer, OrderSerializer, PaymentTypeSerializer, EmployeeSerializer, TrainingSerializer, Emp_TrainSerializer, DepartmentSerializer, ComputerSerializer, Prod_Order_Serializer


###########################################################################
# CUSTOMER SIDE VIEWS
###########################################################################

# Authors Raf and Cashew <3
# Shows the customers view
class customers(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class= CustomerSerializer
    http_method_names = ['get', 'put', 'post']

class Product_TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Product Type to be viewed or edited.
    """
    queryset = Product_Type.objects.all()
    serializer_class = ProductTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Authors Cashew <3
# Shows the Payment_types view
class pay_types(viewsets.ModelViewSet):
    """
    API endpoint that allows Payment_Types to be viewed or edited.
    """
    queryset = Payment_Type.objects.all()
    serializer_class = PaymentTypeSerializer

class orders(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


###########################################################################
# EMPLOYEE SIDE VIEWS
###########################################################################

# Author Raf - EmployeeViewSet
class Employee(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'put', 'post']


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departments to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get', 'put', 'post']

class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Computers to be viewed or edited.
    """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

# Authors: Cashew & Raf <3 - Training_Prog View
class Training_Prog(viewsets.ModelViewSet):
    """
    API endpoint that allows training programs to be viewed or edited.
    """
    queryset = Training_Prog.objects.all()
    serializer_class = TrainingSerializer

# Authors: Cashew & Raf <3 - Emp_Training View
class Emp_Train(viewsets.ModelViewSet):
    """
    API endpoint that allows employee training programs to be viewed or edited.
    """
    queryset = Emp_Training.objects.all()
    serializer_class = Emp_TrainSerializer

class Prod_Order_ViewSet(viewsets.ModelViewSet):
    queryset = Prod_Order.objects.all()
    serializer_class = Prod_Order_Serializer