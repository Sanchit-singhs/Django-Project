from django.contrib import admin
from .models import ReportData, PurchaseRecord, Vendor

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'report_date')

class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')

class InvAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'seller', 'payment_status')

admin.site.register(ReportData, ReportAdmin)
admin.site.register(Vendor, SellerAdmin)
admin.site.register(PurchaseRecord, InvAdmin)