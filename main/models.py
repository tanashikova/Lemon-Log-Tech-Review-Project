from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Review(models.Model):
    title = models.CharField(max_length=50)
    product = models.CharField(max_length=35)
    description = models.CharField(max_length=150)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=300, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("reviews:review_detail", args=[self.slug])

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
       return self.title




class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=240)
    comment_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('comment_date',)


    def __str__(self):
        return f"Comment by{self.user.username}"