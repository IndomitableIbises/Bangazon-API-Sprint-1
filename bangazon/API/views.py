# Authors Raf and Cashew <3

from API.models import Customer
from API.serializers import CustomerSerializer
from rest_framework import viewsets

# Shows the customers view
class customers(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer