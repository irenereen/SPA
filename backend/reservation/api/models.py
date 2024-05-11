from django.db import models
from accounts.api.models import User
from services.api.models import Service
from staff.api.models import Staff

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    staff_member = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Reservation for {self.customer.username} - {self.service.name}"
