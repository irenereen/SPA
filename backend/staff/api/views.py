from rest_framework import generics
from .models import Staff
from .serializers import StaffSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class StaffListCreate(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
