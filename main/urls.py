from django.urls import path 
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('index/', views.reviews_index, name='index'),
     path('reviews/<int:review_id>/', views.reviews_detail, name="review_detail"),
     
]
