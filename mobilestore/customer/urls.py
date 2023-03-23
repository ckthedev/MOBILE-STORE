from django.urls import path
from .views import *

urlpatterns= [
    path('customer/',CustomerHome.as_view(),name='customer'),
    path('pro/<int:pk>',ProductView.as_view(),name='pro'),
    path('addcart/<int:pid>',addcart,name='addcart'),
]