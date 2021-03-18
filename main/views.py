from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import NewCommentForm
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
  comments = review.comments.filter()
  user_comment = None
  if request.method == 'POST':
     comment_form = NewCommentForm(request.POST)
     if comment_form.is_valid():
        user_comment = comment.form.save(commit=False)
        user_comment.review = review
        user_comment.save()
  else:
    comment_form = NewCommentForm()
  return render(request, 'detail.html', 
   {
    "review": review,
    "comments":user_comment, 
    "comments":comments, 
    "comment_form":comment_form,
    },
   )


# def reviews_detail(request, review_id): 
#   review = Review.objects.get(id=review_id) 
#   comments = review.comments.filter()
#   if request.method == 'POST': 
#     comment_form = NewCommentForm(request.POST) 
#     if comment_form.is_valid(): 
#       content = request.POST.get('content') 
#       comment = Comment.objects.create(review = review, user = request.user, content = content) 
#       comment.save() 
#       return redirect(review.get_absolute_url()) 
#     else: 
#       comment_form = NewCommentForm() 
        
#     context ={ 
#       'comment_form':comment_form, 
#       } 
#     return render(request, 'detail.html', context)

       