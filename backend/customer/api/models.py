from django.db import models
from accounts.api.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='customer_profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username
