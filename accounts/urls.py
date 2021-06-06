from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('owner_register/',views.owner_register.as_view(),name='owner_register'),
    path('employee_register/',views.employee_register.as_view(),name='employee_register'),

    ]
