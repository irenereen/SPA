from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.permissions import IsAuthenticated

class ReservationListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
