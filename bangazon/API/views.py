
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from API.models import Product, Product_Type, Customer, Order, Payment_Type, Employee
from API.serializers import ProductSerializer, ProductTypeSerializer, CustomerSerializer, OrderSerializer, PaymentTypeSerializer, EmployeeSerializer


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