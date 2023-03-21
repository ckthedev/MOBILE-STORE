
from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.
class CustomerHome(TemplateView):
    template_name='customer.html'
