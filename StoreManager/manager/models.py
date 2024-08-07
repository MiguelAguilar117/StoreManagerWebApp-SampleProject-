from django.db import models
from django import forms

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subcateggory = models.CharField(max_length=255, null=True)
    brand = models.CharField(max_length=255)
    sku = models.CharField(max_length=15, null=True)
    price = models.FloatField()
    cost = models.FloatField()
    stockQuantity = models.IntegerField()
    reorderLevel = models.IntegerField()
    productImages = models.ImageField(upload_to='products/')
    qr = models.ImageField(upload_to='qr_code/', null=True, blank=True)
    tags = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    
class StoreManager(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"