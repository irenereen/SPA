from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer

User = get_user_model()

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customer(
            email=validated_data['email'],
            username=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.is_customer = True
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)  # Hash the password
        instance.save()
        
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        extra_kwargs = {'password': {'write_only': True}}
        fields=['id','username','address','email','first_name','last_name','phone_number','profile_picture']
    