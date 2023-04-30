
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View,TemplateView,FormView,DetailView
from store.models import Products
from .models import *
from .forms import PaymentForm,OrderForm,ReviewForm
from .models import Cart, Buy
from django.contrib import messages
from django.http import Http404
from django.urls import reverse_lazy

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
        context["form"]=ReviewForm()
        context['review']=Review.objects.all()
        context['pst']=Buy.objects.filter(user=self.request.user)
        return context
def addreview(request, pid):
    if request.method=="POST":
        id = pid
        product = Products.objects.get(id=id)
        user = request.user
        cmnt = request.POST.get("comment")
        Review.objects.create(product=product, user=user, comment=cmnt)
        return redirect('customer')


class MyCart(TemplateView):
    template_name='cart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Cart.objects.all()
        return context

def addcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    mobile=Products.objects.get(id=id)
    user=request.user
    if Cart.objects.filter(mobile=mobile,user=request.user):
        messages.success(request,"already carted")
        return redirect('customer')
    else:
        Cart.objects.create(mobile=mobile,user=user)
        return redirect("customer")





def delcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    user=request.user
    Cart.objects.filter(id=id).delete()
    return redirect('mycart')




class BuyView(TemplateView):
    template_name = 'buy.html'
   

    def post(self, request, *args, **kwargs):
        user = request.user
        products = Cart.objects.filter(user=user).values_list('mobile', flat=True)
        total_cost = sum(Cart.objects.filter(user=user).values_list('mobile__prize', flat=True))
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process payment
            buy = Buy.objects.create(user=user, total_cost=total_cost)
            buy.products.set(products)
            Cart.objects.filter(user=user).delete()
            return redirect('ordersuccess')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)
        
class PaymentView(FormView):
    template_name = 'payment.html'
    form_class = PaymentForm
    success_url = 'ordersuccess'

    def form_valid(self, form):
        # Process payment
        return super().form_valid(form)        

class OrderSuccessView(TemplateView):
    template_name = 'ordersuccess.html'


