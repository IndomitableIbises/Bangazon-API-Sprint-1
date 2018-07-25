from rest_framework import serializers
from API.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'account_date', 'active_inactive', 'last_login', 'first_name', 'last_name')