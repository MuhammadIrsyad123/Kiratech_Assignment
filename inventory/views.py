from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer
from django.shortcuts import render
from .models import Inventory

def inventory_list(request):
    inventories = Inventory.objects.select_related('supplier').all()
    return render(request, 'inventory/list.html', {'inventories': inventories})

def inventory_detail(request, id):
    inventory = Inventory.objects.select_related('supplier').get(id=id)
    return render(request, 'inventory/detail.html', {'inventory': inventory})

class InventoryListAPI(generics.ListAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = Inventory.objects.select_related('supplier').all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
