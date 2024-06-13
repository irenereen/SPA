from django.urls import path
from .views import ObtainTokenView, ProtectedView

urlpatterns = [
    path('token/', ObtainTokenView.as_view(), name='token_obtain'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]