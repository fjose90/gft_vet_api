from customer.models import Customer
from rest_framework import permissions, viewsets

from gft_vet_api.customer.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-date_joined')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
