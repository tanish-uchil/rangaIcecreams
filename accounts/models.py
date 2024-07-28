from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True,max_length=50)
    phone_number = models.CharField(unique=True, max_length=50)
    profile_pic = models.ImageField(upload_to="profile_pic")
    address = models.CharField(max_length=50)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = "Customer"