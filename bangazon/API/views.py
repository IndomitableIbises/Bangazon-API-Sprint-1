
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from API.models import Product, Product_Type, Customer, Order, Payment_Type, Employee, Training_Prog, Emp_Training
from API.serializers import ProductSerializer, ProductTypeSerializer, CustomerSerializer, OrderSerializer, PaymentTypeSerializer, EmployeeSerializer, TrainingSerializer, Emp_TrainSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Authors Raf and Cashew <3
# Shows the customers view
class customers(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class orders(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class Product_TypeViewSet(viewsets.ModelViewSet):

    queryset = Product_Type.objects.all()
    serializer_class = ProductTypeSerializer


# Authors Cashew <3
# Shows the Payment_types view
class pay_types(viewsets.ModelViewSet):
    """
    API endpoint that allows Payment_Types to be viewed or edited.
    """
    queryset = Payment_Type.objects.all()
    serializer_class = PaymentTypeSerializer


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