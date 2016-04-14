from django import forms
from django_summernote.widgets import SummernoteWidget

from posts.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tag_set',
        ]
        widgets = {
            'content': SummernoteWidget(),
            'tag_set': forms.TextInput(),
        }


class PostUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        tags = kwargs['instance'].tag_set.all()
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        tag_name_list = [tag.name for tag in tags]
        self.fields['tag_set'] = forms.CharField(initial={'subject': " ".join(tag_name_list)})

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tag_set',
        ]
        widgets = {
            'content': SummernoteWidget(),
        }
