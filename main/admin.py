from django.contrib import admin
from . import models 

@admin.register(models.Review)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'slug', 'user')
    prepopulated_fields = {
        "slug":("title",),
    }


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'title', 'user', 'comment_date', 'status')



