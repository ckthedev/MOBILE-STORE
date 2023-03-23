
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from store.models import Products
from .models import *

# Create your views here.
class CustomerHome(TemplateView):
    template_name='customer.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.all()
        return context

class ProductView(TemplateView):
    template_name='product.html'
    def get_context_data(self, **kwargs):
        id=kwargs.get('pk')
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.get(id=id)
        return context

def addcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    mobile=Products.objects.get(id=id)
    user=request.user
    Cart.objects.create(mobile=mobile,user=user)
    return redirect('customer')