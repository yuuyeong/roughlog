from django.shortcuts import redirect
from django.views.generic import View

from posts.models import Post, Comment


class CreateCommentView(View):
    def post(self, request, *args, **kwargs):
        inputed_content = request.POST.get('content')
        post = Post.objects.get(pk=kwargs.get('pk'))
        comment = Comment.objects.create(
            user=request.user,
            post=post,
            content=inputed_content,
        )

        return redirect(comment)
