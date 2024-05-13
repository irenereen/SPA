from rest_framework import serializers
from .models import Reservation
from .models import Reservation
from services.api.models import Service

class ReservationSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)

    class Meta:
        model = Reservation
        fields = ['id', 'customer', 'services', 'staff_member', 'date_time', 'status', 'cost']
        read_only_fields = ['cost']
        

    def create(self, validated_data):
        services = validated_data.pop('services')
        appointment = Reservation.objects.create(**validated_data)
        appointment.services.set(services)
        appointment.cost = sum(service.price for service in services)
        appointment.save()
        return appointment

    def update(self, instance, validated_data):
        services = validated_data.pop('services', None)
        if services is not None:
            instance.services.set(services)
            instance.cost = sum(service.price for service in services)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance