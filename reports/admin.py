from django.contrib import admin
from .models import Report, Sales_record, Seller

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'report_type', 'report_date')

class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')

class InvAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'seller')

admin.site.register(Report, ReportAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Sales_record, InvAdmin)