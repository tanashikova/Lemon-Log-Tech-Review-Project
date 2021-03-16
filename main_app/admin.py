from django.contrib import admin
# import your models here
from .models import Product, Profile

# Register your models here
admin.site.register(Product)
admin.site.register(Profile)