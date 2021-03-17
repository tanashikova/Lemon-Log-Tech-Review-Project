from django.shortcuts import render, redirect
from .models import Product


def products_index(request):
  products = Product.objects.all()
  return render(request, 'products/index.html', { 'products': products })

