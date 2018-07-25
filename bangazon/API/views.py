from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from API.models import Product
from API.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    def product_list(request):

        if request.method == 'GET':
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)

        # elif request.method == 'POST':
        #     data = JSONParser().parse(request)
        #     serializer = ProductSerializer(data=data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return JsonResponse(serializer.data, status=201)
        #     return JsonResponse(serializer.errors, status=400)

