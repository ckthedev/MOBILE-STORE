from django.urls import path
from .views import Mainhome,CustomerHomeView,StoreHomeView

urlpatterns = [
    path("Mainhome/",Mainhome.as_view(),name="Mainhome"),
    path('customer/', CustomerHomeView.as_view(), name='customer'),
    path('store/', StoreHomeView.as_view(), name='store'),
    
]
