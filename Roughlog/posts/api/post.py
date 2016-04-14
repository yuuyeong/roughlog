from rest_framework.generics import ListAPIView

from django.contrib.auth import get_user_model

from posts.serializers import PostSerializer


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = get_user_model().objects.get(
            nickname=self.request.user.nickname
        )
        return user.post_set.all()

    # 새로운 포스트를 저장
    def post(self, request, *args, **kwargs):
        pass
