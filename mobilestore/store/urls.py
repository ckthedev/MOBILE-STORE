from django.urls import path
from .views import *

urlpatterns=[
    path('store/',StoreHome.as_view(),name='store'),
      path('addproduct/',AddProduct.as_view(),name='addproduct'),
    path('myproduct/',MyProducts.as_view(),name='myproduct'),
    path('updatepro/<int:pk>/',UpdateProduct.as_view(),name='updatepro'),
    path('deletepro/<int:pk>/',DeleteProduct.as_view(),name='deletepro'),
]