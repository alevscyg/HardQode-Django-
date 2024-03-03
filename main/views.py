from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()
    return render(request, 'main/products.html',{'products':products})
def auth(request):
    return render(request, 'main/auth.html')