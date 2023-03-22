# Generated by Django 4.1.7 on 2023-03-16 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0004_remove_order_log_remove_orderitem_log_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='order',
        #     name='log',
        # ),
        # migrations.RemoveField(
        #     model_name='orderitem',
        #     name='log',
        # ),
        # migrations.RemoveField(
        #     model_name='product',
        #     name='log',
        # ),
        # migrations.AddField(
        #     model_name='order',
        #     name='created_by',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        # ),
        # migrations.AddField(
        #     model_name='order',
        #     name='deleted_at',
        #     field=models.DateTimeField(blank=True, null=True),
        # ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        # migrations.AddField(
        #     model_name='order',
        #     name='updated_by',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        # ),
        # migrations.AddField(
        #     model_name='orderitem',
        #     name='created_by',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        # ),
        # migrations.AddField(
        #     model_name='orderitem',
        #     name='deleted_at',
        #     field=models.DateTimeField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name='orderitem',
        #     name='updated_at',
        #     field=models.DateTimeField(auto_now=True),
        # ),
        # migrations.AddField(
        #     model_name='orderitem',
        #     name='updated_by',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        # ),
        # migrations.AddField(
        #     model_name='product',
        #     name='created_by',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        # ),
        # migrations.AddField(
        #     model_name='product',
        #     name='deleted_at',
        #     field=models.DateTimeField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name='product',
        #     name='updated_at',
        #     field=models.DateTimeField(auto_now=True),
        # ),
        # migrations.AddField(
        #     model_name='product',
        #     name='updated_by',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        # ),
        # migrations.AlterField(
        #     model_name='orderitem',
        #     name='order',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.order'),
        # ),
    ]