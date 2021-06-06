from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from .models import User
from .form import  EmployeeSignUpForm,OwnerSignUpForm
from django.contrib.auth import login, logout,authenticate

# Create your views here.

class owner_register(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = "register/owner_register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = "register/employee_register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

