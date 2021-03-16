from django.urls import path 
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('products/', views.products_index, name='index'),
     path('profile/', views.profile, name='profile'),
     path('register/', views.register, name='register'),
]