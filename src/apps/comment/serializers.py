from rest_framework import serializers

from src.apps.comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer комментария с полной информацией о нем"""

    class Meta:
        model = Comment
        fields = "__all__"
