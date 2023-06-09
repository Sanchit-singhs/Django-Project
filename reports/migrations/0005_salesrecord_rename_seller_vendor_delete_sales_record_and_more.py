# Generated by Django 4.1.7 on 2023-03-22 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_order_log_remove_orderitem_log_and_more'),
        ('reports', '0004_rename_product_name_sales_record_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete')], default='pending', max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.RenameModel(
            old_name='Seller',
            new_name='Vendor',
        ),
        migrations.DeleteModel(
            name='Sales_record',
        ),
        migrations.AddField(
            model_name='salesrecord',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.vendor'),
        ),
    ]
