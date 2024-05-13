from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.permissions import IsAdminUser

class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
