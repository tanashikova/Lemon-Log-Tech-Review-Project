from django.db import models

# Create your models here.
class Product:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, brand, description, yr):
    self.name = name
    self.brand = brand
    self.description = description
    self.yr = yr

products = [
  Product('iphone x', 'apple', 'smart phone', 2021),
  Product('smart tv', 'LG', '55 inch flatscreen with smart hub', 2019),
  Product('wireless mouse', 'Philips', 'wireless mouse with usb dongle', 2020)
]