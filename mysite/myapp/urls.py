from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('clicker/', views.clicker, name='clicker'),
    path('calculator/', views.calculator, name='calculator'),
    path('about/', views.about, name='about'),
]
