from django.shortcuts import render, redirect
from .models import Product


def home(request):
  return render(request, 'home.html' )

def about(request):
  return render(request, 'about.html')

def products_index(request):
  products = Product.objects.all()
  return render(request, 'products/index.html', { 'products': products })

