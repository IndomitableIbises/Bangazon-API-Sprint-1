from API.models import Customer
from API.serializers import CustomerSerializer
from rest_framework import viewsets


class customers(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# class customer_list(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Customers.objects.all()
#     serializer_class = GroupSerializer