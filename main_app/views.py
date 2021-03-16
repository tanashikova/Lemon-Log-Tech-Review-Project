from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def home(request):
  return render(request, 'home.html' )

def about(request):
  return render(request, 'about.html')

def products_index(request):
  products = Product.objects.all()
  return render(request, 'products/index.html', { 'products': products })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile/user.html')