from django import forms
from django_summernote.widgets import SummernoteWidget

from posts.models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'article',
        ]
        widgets = {
            'content': SummernoteWidget(),
        }
