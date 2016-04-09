from django.shortcuts import redirect
from django.views.generic import View

from posts.models import Clip, Post


class PostClipView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(pk=kwargs.get("pk"))

        clip, is_created = Clip.objects.get_or_create(
            user=user,
            post=post,
        )

        # 이미 좋아요를 누른 상태라면 삭제한다.
        if not is_created:
            clip.delete()

        return redirect(post)
