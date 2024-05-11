from rest_framework import serializers
from .models import Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'user', 'role', 'shift_start_time', 'shift_end_time']
