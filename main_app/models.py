from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    manufactoring_year = models.IntegerField()
    # review = models.ForeignKey(Review, on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.TextField(max_length=240)
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default = "default.jpg", upload_to='profile_pics')
    

    def __str__(self):
        return f'{self.user.username} Profile'

class Review(models.Model):
    title = models.CharField(max_length=50)
    product = models.CharField(max_length=35)
    description = models.CharField(max_length=150)
    rating = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

