from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import Review, Comment, Photo

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review, Comment
from django.views.generic import DeleteView


from .forms import NewCommentForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'lemonlog3'


def add_photo(request, review_id):
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



# <form action="{% url 'add_photo' review.id %}" enctype="multipart/form-data" method="POST" class="card-panel">
#               {% csrf_token %}
#               <input type="file" name="photo-file">
#               <br><br>
#               <input type="submit" class="btn" value="Upload Photo">
#             </form>


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
    success_url = '/'

    def test_func(self):
      comment = self.get_object()
      if self.request.user == comment.user:
        return True
      return False


