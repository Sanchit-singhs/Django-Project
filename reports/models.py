from django.db import models
from inventory.models import Product
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class ReportData(models.Model):
    REPORT_TYPE_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    )
    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES, default='daily')
    report_date = models.DateField()
    report_data = models.TextField()


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True, null=True)
    address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class PurchaseRecord(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('complete', 'Complete'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    seller = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')

    # def save(self, *args, **kwargs):
    #     super(SalesRecord, self).save(*args, **kwargs)
    #     product = self.product
    #     product.quantity += self.quantity
    #     product.save()
