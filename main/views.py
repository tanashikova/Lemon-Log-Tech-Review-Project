from django.shortcuts import render, redirect
from .models import Review, Comment

def home(request):
  reviews = Review.objects.all()
  return render(request, 'home.html' , {"reviews": reviews })

def about(request):
  return render(request, 'about.html')

def reviews_index(request):
  reviews = Review.objects.all()
  print(reviews)
  return render(request, 'index.html', { 'reviews': reviews })


# add comment
def add_comment(request, slug):
    if request.user.is_authenticated:
        review = Review.objects.get(slug=slug)
        if request.method == 'POST':
            form = PostForm(request.POST or None)
            if form.is_valid():
                com = form.save(commit=False)
                com.review = review
                com.user = request.user
                com.save()
                return redirect("home")
        else:
            form = PostForm(request.POST or None)
        return render(request, 'comment.html', {'form': form})
    else:
        return redirect("login_user")

