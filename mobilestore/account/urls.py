from django.urls import path
from .views import home_view,Reg,LogView,LogOut

urlpatterns = [
    path('', home_view.as_view(), name='home'),
    path('reg/', Reg.as_view(), name='reg'),
     path('log/', LogView.as_view(), name='log'),
     path('logout/',LogOut.as_view(),name='lgout')
]
