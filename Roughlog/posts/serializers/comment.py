from posts.models import Comment

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    comment_writer = serializers.CharField(source="user.nickname")

    class Meta:
        model = Comment
        fields = ('id', 'content', 'comment_writer',)
