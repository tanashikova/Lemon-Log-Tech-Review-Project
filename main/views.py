from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review, Comment
from django.views.generic import DeleteView

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
# def reviews_detail(request, review_id):
#   reviews = Review.objects.get(id=review_id)
#   return render(request, 'detail.html', { 'reviews': reviews })

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



def edit_comment(request, review_id, comment_id):
  review = Review.objects.get(id=review_id)
  comment = Comment.objects.get(id=comment_id)
  edit_form = NewCommentForm(request.POST or None, instance=comment)
  if request.POST and edit_form.is_valid():
    edit_form.save()
    return redirect('review_detail', review_id = review_id)
  else:
    return render(request, 'edit.html',{'edit_form': edit_form, 'review':review, 'comment':comment })


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = 'review_detail'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False