from django.shortcuts import render, redirect
from .models import Review

def home(request):
  reviews = Review.objects.all()
  return render(request, 'home.html' , {"reviews": reviews })

def about(request):
  return render(request, 'about.html')

def reviews_index(request):
  reviews = Review.objects.all()
  return render(request, 'index.html', { 'reviews': reviews })

def reviews_detail(request, review_id):
  review = Review.objects.get(id=review_id)
  return render(request, 'detail.html', {'review': review })
