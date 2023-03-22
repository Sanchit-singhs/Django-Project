from django.db import models
from inventory.models import Product
# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_type = models.CharField(max_length=50)
    report_date = models.DateField()
    report_data = models.TextField()


class Seller(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True, null=True)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Sales_record(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)