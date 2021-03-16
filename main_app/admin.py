from django.contrib import admin
# import your models here
from .models import Product, Profile, Review, Comment

# Register your models here
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Comment)