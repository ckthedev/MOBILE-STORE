from django.db import models
from account.models import CustUser

# Create your models here.

class Products(models.Model):
    Mobile=models.ImageField(upload_to="product_image",null=True)
    Name=models.CharField(max_length=100)
    prize=models.IntegerField()
    ram=models.IntegerField(null=True)
    rom=models.IntegerField(null=True)
    processer=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="m_store")