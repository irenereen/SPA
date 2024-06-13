from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.TextField(max_length=50, null=True)
    profile_picture = models.ImageField(upload_to='customer_profile_pics', blank=True, null=True)
    is_customer = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_user_set',  # Avoid clash with 'auth.User'
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='customer'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_user_set',  # Avoid clash with 'auth.User'
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customer',
    )

    def __str__(self):
        return self.username
