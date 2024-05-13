from django.db import models
from accounts.api.models import User
from services.api.models import Service
from staff.api.models import Staff

class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    staff_member = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Appointment for {self.customer.username} - {', '.join([service.name for service in self.services.all()])}"