from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
      email = models.EmailField(unique=True)
      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['email']
      
      groups = models.ManyToManyField('auth.Group', related_name='custom_user_set')
      user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set')
      def __str__(self):
            return self.email
