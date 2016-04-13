from django.shortcuts import redirect
from django.views.generic import FormView

from posts.models import Post
from posts.forms import PostCreateForm
from tags.models import Tag
from articles.models import Pocket


class NewPostCreateView(FormView):
    template_name = 'posts/new.html'
    form_class = PostCreateForm
    slug_field = "pk"

    def post(self, request, *args, **kwargs):
        pocket = Pocket.objects.get(pk=kwargs.get("pk"))
        tag_list = request.POST.get('tag').split(" ")

        post = Post.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            article=pocket.article,
        )

        for tag_name in tag_list:
            if tag_name is "":
                continue
            tag, is_created = Tag.objects.get_or_create(
                name=tag_name,
            )
            post.tag_set.add(tag)
        return redirect(post)
