from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializer import TokenObtainSerializer
from accounts.api.serializers import CustomerSerializer, ProfileSerializer
from accounts.api.models import Customer



class ObtainTokenView(APIView):
    def post(self, request):
        serializer = TokenObtainSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = Customer.objects.filter(email=email).first()
            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user':user.id
                })
            return Response({"error": "Invalid credentials"}, status=400)
        return Response(serializer.errors, status=400)

class ProtectedView(RetrieveAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    def get_object(self):
        user = self.request.user
        print(user)
        return Customer.objects.get()
