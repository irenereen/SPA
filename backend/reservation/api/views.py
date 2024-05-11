from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
