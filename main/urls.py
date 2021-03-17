from django.urls import path 
from . import views

urlpatterns = [
     path('products/', views.products_index, name='index'),
     # path('review/<>')
]
