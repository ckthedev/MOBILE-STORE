from django.urls import path
from .views import *

urlpatterns=[
    path('store/',StoreHome.as_view(),name='store')
]