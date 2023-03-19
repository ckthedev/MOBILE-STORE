from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView


class Mainhome(TemplateView):
    template_name="Mainhome.html"



class CustomerHomeView(View):
    def get(self, request):
        return render('customer.html')    

class StoreHomeView(View):
    def get(self, request):
        return render('store.html')

