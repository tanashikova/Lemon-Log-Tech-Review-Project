from django.urls import path 
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('reviews/', views.reviews_index, name='index'),
     path(r'reviews/<int:review_id>/', views.reviews_detail, name="review_detail")
]
