from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)
    code_type = models.CharField(max_length=10)  # To store whether it's a QR code or Barcode
    created_at = models.DateTimeField(default=timezone.now)  # Timestamp for when the product was added

    def __str__(self):
        return self.name
