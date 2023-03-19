from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustUser(AbstractUser):
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=500,null=True)
    image=models.ImageField(upload_to="profile_image",null=True)
    options=(

        ("Store","Store"),
        ("Customer","Customer"),
    )

    usertype=models.CharField(max_length=100,choices=options,default="Customer")



# class Mobile(models.Model):
#     name = models.CharField(max_length=255)
#     brand = models.CharField(max_length=255)
#     price = models.FloatField()
#     description = models.TextField()
#     image = models.ImageField(upload_to='mobile_images/', default='mobile_images/default.jpg')

#     def __str__(self):
#         return self.name





