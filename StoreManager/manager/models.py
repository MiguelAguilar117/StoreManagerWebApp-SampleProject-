from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subcateggory = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    sku = models.CharField(max_length=15)
    price = models.FloatField()
    cost = models.FloatField()
    stockQuantity = models.IntegerField()
    reorderLevel = models.IntegerField()
    supplierId = models.IntegerField(null=True)
    productImages = models.ImageField(upload_to='products/')
    qr = models.ImageField(upload_to='qr_code/', null=True, blank=True)
    tags = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255)

