from django.db import models
from accounts.api.models import Customer

class Staff(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('therapist', 'Therapist'),
        ('receptionist', 'Receptionist'),
        ('hairdresser', 'Hairdresser')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()

    def __str__(self):
        return f"{self.customer.username} - {self.role}"
