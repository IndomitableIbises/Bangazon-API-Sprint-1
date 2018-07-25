from rest_framework import serializers
from API.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description', 'quanity')



# 'customer_id', 'type_id'


