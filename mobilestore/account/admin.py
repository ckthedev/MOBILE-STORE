from django.contrib import admin
from django.db import models

# Register your models here.

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     description = models.TextField()

# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     customer_name = models.CharField(max_length=100)
#     customer_email = models.EmailField()