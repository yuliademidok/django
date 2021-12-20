from rest_framework import serializers

from likes_app.api.serializers.like import LikeSerializer
from ...models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "likes"]
        read_only_fields = ["id", ]

    likes = LikeSerializer(many=True, read_only=True)
