from django.urls import path
from .views import InventoryListAPI,inventory_list, inventory_detail

urlpatterns = [
    path('api/inventory/', InventoryListAPI.as_view(), name='inventory-api'),
    path('inventory/', inventory_list, name='inventory-list'),
    path('inventory/<int:id>/', inventory_detail, name='inventory-detail'),
]