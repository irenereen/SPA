from django.db import models
from accounts.api.models import User


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('therapist', 'Therapist'),
        ('receptionist', 'Receptionist'),
        ('hairdreser', 'Hairdreser')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.role}"
