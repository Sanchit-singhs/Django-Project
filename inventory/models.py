from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class BaseModel(models.Model):
    created_by = models.ForeignKey('Admin_panel.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    updated_by = models.ForeignKey('Admin_panel.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

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
    customer_email = models.EmailField(unique=True)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order {self.customer_email}"
    
class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.price = self.product.price
        self.total_price = self.quantity * self.price
        super(OrderItem, self).save(*args, **kwargs)
        # order = self.order
        # order.total_bill = sum(item.total_price for item in order.items.all())
        # order.save()

    def __str__(self):
        return f'Name: {self.order.customer_name} Order: {self.product}'
    
