from django import forms
from django_summernote.widgets import SummernoteWidget


# class PostCreateForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = [
#             'title',
#             'content',
#             'article',
#         ]
#         widgets = {
#             'content': SummernoteWidget(),
#         }

class PostCreateForm(forms.Form):
    title = forms.CharField(label='제목')
    content = forms.CharField(
        widget=SummernoteWidget(),
        label='본문'
    )
    tag = forms.CharField(
        required=False,
        label='태그'
    )
    url = forms.URLField(
        label='아티클',
    )
