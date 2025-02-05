from django.test import TestCase, Client
from django.urls import reverse
from .models import Supplier, Inventory

class InventoryTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.inventory = Inventory.objects.create(
            name="Test Item",
            description="Test Description",
            note="Test Note",
            stock=10,
            availability=True,
            supplier=self.supplier
        )

    def test_inventory_list_page(self):
        response = self.client.get(reverse('inventory-list'))
        self.assertEqual(response.status_code, 200)

    def test_api_endpoint(self):
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_page(self):
        response = self.client.get(reverse('inventory-detail', args=[self.inventory.id]))
        self.assertEqual(response.status_code, 200)