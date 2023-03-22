from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)

