from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author','published_date','is_deleted','categories')
        widgets = {
            "time_to_read" : forms.TextInput(attrs={"class":"input"}),
            "title" : forms.TextInput(attrs={'class':"input"}),
            "short_description" : forms.Textarea(attrs={'class':"input"}),
        }