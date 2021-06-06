from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView
# Create your views here.

class index(TemplateView):
    template_name = "pages/index.html"

    