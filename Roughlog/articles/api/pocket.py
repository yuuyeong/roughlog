from rest_framework.generics import ListAPIView

from django.contrib.auth import get_user_model
from articles.serializers import PocketSerializer


class PocketListAPIView(ListAPIView):
    serializer_class = PocketSerializer

    def get_queryset(self):
        user = get_user_model().objects.get(
            nickname=self.request.user.nickname
        )
        return user.pocket_set.all()

    # 새로운 포켓을 저장
    def post(self, request, *args, **kwargs):
        pass
