from django.db import models
from account.models import CustUser
from store.models import Products
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    mobile=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='m_cart',null=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='u_cart')

class Review(models.Model):
    comment=models.CharField(max_length=200)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='commented_user')
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='commented_product')

class Buy(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)    


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
