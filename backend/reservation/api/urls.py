from django.urls import path
from .views import ReservationListCreate, ReservationRetrieveUpdateDestroy

urlpatterns = [
    path('', ReservationListCreate.as_view(), name='reservation-list-create'),
    path('<int:pk>/', ReservationRetrieveUpdateDestroy.as_view(), name='reservation-detail'),
]
