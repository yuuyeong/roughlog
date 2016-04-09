from django.shortcuts import redirect
from django.views.generic import View

from posts.models import Post
from tags.models import Tag


class CreateTagView(View):
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))
        tag, is_created = Tag.objects.get_or_create(
            name=request.POST.get('tag_name'),
        )
        post.tag_set.add(tag)

        return redirect(post)
