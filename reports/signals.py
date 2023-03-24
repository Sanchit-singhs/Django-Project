from reports.models import PurchaseRecord
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=PurchaseRecord)
def update_product_quantity(sender, instance, **kwargs):
    product = instance.product
    product.quantity += instance.quantity
    product.save()