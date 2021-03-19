from django import forms
from .models import Comment

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content')
        widgets = {
            "name" : forms.TextInput(attrs={"class": "col-sm-12"}),
            "content" : forms.Textarea(attrs={"class": "form-control"}),
        }
       