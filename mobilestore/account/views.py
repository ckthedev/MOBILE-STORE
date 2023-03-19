from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import RegForm,LogForm
from .models import CustUser
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate,login


class home_view(TemplateView):
    template_name = 'home.html'


class Reg(CreateView):
    template_name = 'reg.html'
    form_class = RegForm
    model = CustUser
    success_url = reverse_lazy('home')

class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    
    def post(self, req, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                messages.success(req, "Login SuccessFull!!")
                return redirect("Mainhome")
            else:
                messages.error(req, "Login Failed!!")
                return render("log.html", {"form": form})
        else:
            return self.form_invalid(form)



