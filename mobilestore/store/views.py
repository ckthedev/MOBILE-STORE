from django.shortcuts import render
from django.views.generic import View,TemplateView,CreateView
from .models import Products
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class StoreHome(CreateView):
    form_class=ProductForm
    model=Products
    template_name='store.html'
    success_url=reverse_lazy('store')
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        return super().form_valid(form)