from django.urls import path
from .views import *

urlpatterns=[
    path('customer/',CustomerHome.as_view(),name='customer')
]