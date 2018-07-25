# Authors Raf and Cashew <3

from rest_framework import serializers
from API.models import Customer

# Translates database into json format
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'account_date', 'active', 'last_login', 'first_name', 'last_name')