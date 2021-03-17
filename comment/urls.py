from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='comment-home'),
    path('about/', views.about, name='comment-about'),
]
