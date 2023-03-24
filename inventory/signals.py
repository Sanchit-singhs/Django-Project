from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem
from django.db.models import Sum


@receiver(post_save, sender=OrderItem)
def update_order_total_bill(sender, instance, **kwargs):
    order = instance.order
    # order.total_bill = sum(item.total_price for item in order.items.all())
    order.total_bill = OrderItem.objects.filter(order=order).aggregate(total_price=Sum('total_price'))['total_price']
    order.save()

@receiver(post_save, sender=OrderItem)
def update_product_quantity(sender, instance, **kwargs):
    product = instance.product
    product.quantity -= instance.quantity
    product.save()
