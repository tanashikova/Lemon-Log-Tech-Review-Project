from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Product:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, brand, description, yr):
    self.name = name
    self.brand = brand
    self.description = description
    self.yr = yr
    

products = [
  Product('iphone x', 'Apple', 'smart phone', 2021),
  Product('smart tv', 'LG', '55 inch flatscreen with smart hub', 2019),
  Product('wireless mouse', 'Philips', 'wireless mouse with usb dongle', 2020)
]

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def products_index(request):
  return render(request, 'products/index.html', { 'products': products })