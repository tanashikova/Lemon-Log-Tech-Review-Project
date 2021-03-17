from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    manufactoring_year = models.IntegerField()
    # review = models.ForeignKey(Review, on_delete=models.CASCADE)


