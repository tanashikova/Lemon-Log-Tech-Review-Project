from django.urls import path 
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('index/', views.reviews_index, name='index'),
     path('reviews/<int:review_id>/', views.reviews_detail, name="review_detail"),
     path('reviews/<int:review_id>/edit_comment/<int:comment_id>/edit/', views.edit_comment, name="edit"),
     # path('reviews/<int:review_id>/delete_comment/<int:comment_id>/delete/', views.delete_comment, name="delete"),
     
]
