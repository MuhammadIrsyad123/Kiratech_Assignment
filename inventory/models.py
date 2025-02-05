from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name