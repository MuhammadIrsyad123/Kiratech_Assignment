from django.contrib import admin
from .models import Inventory, Supplier

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'stock', 'availability')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)