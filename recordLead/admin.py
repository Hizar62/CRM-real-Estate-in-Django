from django.contrib import admin
from .models import Lead
# Register your models here.
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name', 'property_type', 'property_area','property_price','schedule')