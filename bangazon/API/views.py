
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from API.models import Product, Product_Type, Customer, Payment_Type
from API.serializers import ProductSerializer, ProductTypeSerializer, CustomerSerializer, PaymentTypeSerializer

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