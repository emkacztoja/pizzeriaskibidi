from django.shortcuts import render
from .models import Service

def home(request):
    return render(request, 'myapp/home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'myapp/services.html', {'services': services})

def clicker(request):
    return render(request, 'myapp/clicker.html')

def calculator(request):
    return render(request, 'myapp/calculator.html')

def about(request):
    return render(request, 'myapp/about.html')
