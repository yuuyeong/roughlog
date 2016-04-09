from django.shortcuts import redirect
from django.views.generic import FormView

from posts.models import Post
from posts.forms import PostCreateForm
from tags.models import Tag


class NewPostCreateView(FormView):
    template_name = 'posts/new.html'
    form_class = PostCreateForm

    def post(self, request, *args, **kwargs):
        tag_list = request.POST.get('tag').split(" ")

        post = Post.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            content=request.POST.get('content'),
        )

        for tag_name in tag_list:
            tag, is_created = Tag.objects.get_or_create(
                name=tag_name,
            )
            post.tag_set.add(tag)
        return redirect(post)
