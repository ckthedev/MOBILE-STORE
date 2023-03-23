from django.shortcuts import render
from django.views.generic import View,TemplateView,CreateView,UpdateView,DeleteView
from .models import Products
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class StoreHome(TemplateView):
    template_name='store.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.all()
        return context

class AddProduct(CreateView):
    form_class=ProductForm
    model=Products
    template_name='addproduct.html'
    success_url=reverse_lazy('store')
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        return super().form_valid(form)
    
class UpdateProduct(UpdateView):
    form_class=ProductForm
    model=Products
    template_name='addproduct.html'
    success_url=reverse_lazy('store')

class MyProducts(TemplateView):
    template_name="myproduct.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.filter(user=self.request.user)
        return context

class DeleteProduct(DeleteView):
    model=Products
    template_name='deleteproduct.html'
    success_url=reverse_lazy('myproduct')