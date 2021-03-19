from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Review, Comment
from .forms import NewCommentForm
from django.contrib.auth.decorators import login_required
# from django.urls import reverse
def home(request):
  reviews = Review.objects.all()
  return render(request, 'home.html' , {"reviews": reviews })

def about(request):
  return render(request, 'about.html')
@login_required
def reviews_index(request):
  reviews = Review.objects.all()
  return render(request, 'index.html', { 'reviews': reviews })

@login_required
def reviews_detail(request, review_id):
  review = Review.objects.get(id=review_id)
  comment_form = NewCommentForm(request.POST or None)
  comments = review.comments.filter(status=True)
  user_comment = None
  if request.POST and comment_form.is_valid():
    user_comment = comment_form.save(commit=False)
    user_comment.review = review
    user_comment.user = request.user
    user_comment.save()
    return redirect('review_detail', review_id=review_id) 
  else:
    return render(request, 'detail.html', {'review':review, 'user_comment': user_comment, 'comments':comments, 'comment_form': comment_form})


       