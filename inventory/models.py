from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    code_type = models.CharField(max_length=10)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
