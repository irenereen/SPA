from rest_framework import serializers
from .models import Customer
from accounts.api.serializers import UserSerializer

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone_number', 'address', 'profile_picture']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        customer, created = Customer.objects.update_or_create(user=user, **validated_data)
        return customer
