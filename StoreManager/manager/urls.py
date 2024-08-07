from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('sign_in/', views.sign_up, name='sign_in'),
    #path('success', lambda request: render(request, 'template.html'), name='success')
    path('template/', views.testing, name='template'),
]