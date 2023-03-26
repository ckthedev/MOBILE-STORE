from django.urls import path
from .views import *

urlpatterns= [
    path('customer/',CustomerHome.as_view(),name='customer'),
    path('product/<int:pk>',ProductView.as_view(),name='product'),
    path('MyCart/',MyCart.as_view(),name="mycart"),
    path('addcart/<int:pid>',addcart,name='addcart'),
    path('delcart/<int:pid>',delcart,name='delcart'),
    path('buy/<int:pid>', BuyView.as_view(), name='buy'),
    path('ordersuccess/', OrderSuccessView.as_view(), name='ordersuccess'),
    path('review/<int:pid>/', addreview, name='addr'),
  
]