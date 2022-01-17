from rest_framework import serializers

from likes_app.api.serializers.like import LikeSerializer, LikePostSerializer
from tag_app.api.serializers.tag import TagSerializer
from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["id", "user", ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )

    tags = TagSerializer(many=True, read_only=True)

    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, instance) -> int:
        return instance.likes.count()

    likes = LikePostSerializer(many=True, read_only=True)

    def get_comments_count(self, instance) -> int:
        return instance.comments.count()
