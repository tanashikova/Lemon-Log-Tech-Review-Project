from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=50)
    product = models.CharField(max_length=35)
    description = models.CharField(max_length=150)
    rating = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)