
from rest_framework import serializers



class TokenObtainSerializer(serializers.Serializer):      
    
    email = serializers.EmailField()
    password = serializers.CharField()
