from django import forms
from .models import Comment

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'name', 'content')
        # widgets = {
        #     "user" = forms.TextInput(attrs={"class":"col-sm-12"}),
        #     "name" = forms.TextInput(attrs={"class":"col-sm-12"}),
        #     "content" = forms.Textarea(attrs={"class":"form-control"}),
        # }
       