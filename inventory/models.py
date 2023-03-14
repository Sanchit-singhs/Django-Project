from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    log = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(BaseModel):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.pk}"


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.price
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} @ {self.price} = {self.total_price}'
