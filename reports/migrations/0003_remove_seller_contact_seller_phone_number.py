# Generated by Django 4.1.7 on 2023-03-15 05:13

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_seller_sales_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='contact',
        ),
        migrations.AddField(
            model_name='seller',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]