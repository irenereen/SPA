from django.urls import path, include
from .views import ServiceListCreate, ServiceRetrieveUpdateDestroy

urlpatterns = [
    path('', ServiceListCreate.as_view(), name='service-list-create'),
    path('<int:pk>/', ServiceRetrieveUpdateDestroy.as_view(), name='service-detail'),
]