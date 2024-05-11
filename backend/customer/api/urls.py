from django.urls import path
from .views import CustomerListCreate, CustomerRetrieveUpdateDestroy

urlpatterns = [
    path('', CustomerListCreate.as_view(), name='customer-list-create'),
    path('<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-detail'),
]
