from django.contrib import admin
from .models import Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'total_bill')
    inlines = [OrderItemInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity')
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)

