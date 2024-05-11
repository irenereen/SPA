from django.urls import path
from .views import StaffListCreate, StaffRetrieveUpdateDestroy

urlpatterns = [
    path('', StaffListCreate.as_view(), name='staff-list-create'),
    path('<int:pk>/', StaffRetrieveUpdateDestroy.as_view(), name='staff-detail'),
]
