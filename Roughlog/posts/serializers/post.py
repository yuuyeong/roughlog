from posts.models import Post

from rest_framework import serializers

from .comment import CommentSerializer


class PostBaseSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source="user.nickname")

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'nickname')


class PostSerializer(PostBaseSerializer):
    pass


# class PostDetailSerializer(PostBaseSerializer):
#     comments = CommentSerializer(source="comment_set.all", many=True,)

#     class Meta(PostBaseSerializer.Meta):
#         fields =  PostBaseSerializer.Meta.fields + (
#             'comments',
#         )
