from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=50)
    product = models.CharField(max_length=35)
    description = models.CharField(max_length=150)
    rating = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField(max_length=240)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username