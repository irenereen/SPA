from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Customer
from .serializers import CustomerSerializer, ProfileSerializer

class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = ProfileSerializer
    