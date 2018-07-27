
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from API.models import Product, Department
from API.serializers import ProductSerializer, DepartmentSerializer
from API.models import Customer
from API.serializers import CustomerSerializer
from API.models import Product, Product_Type, Order, Customer
from API.serializers import ProductSerializer, ProductTypeSerializer, CustomerSerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Authors Raf and Cashew <3

# Shows the customers view
class customers(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class orders(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class Product_TypeViewSet(viewsets.ModelViewSet):

    queryset = Product_Type.objects.all()
    serializer_class = ProductTypeSerializer

