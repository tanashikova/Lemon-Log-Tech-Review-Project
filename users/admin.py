from django.contrib import admin
from .models import Profile
from main.models import Photo

admin.site.register(Profile)
admin.site.register(Photo)
