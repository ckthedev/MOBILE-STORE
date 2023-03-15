from django.shortcuts import render
from django.views.generic import View,TemplateView

class home_view(TemplateView):
    template_name = 'home.html'
