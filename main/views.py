from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import NewCommentForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'lemonlog3'

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
        return render(request, 'detail.html')
  else:
    comment_form = NewCommentForm()
  return render(request, 'detail.html', {'review': review, 'comments':user_comment, 'comments':comments})

def add_photo(request, profile_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, review_id=review_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', review_id=review_id)
       