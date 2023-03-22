from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'address', 'phone_number')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('address', 'phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
