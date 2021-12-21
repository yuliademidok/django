from rest_framework import serializers

from ...models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        # fields = ["post"]
        exclude = ["user", "comment", ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        # fields = ["comment"]
        exclude = ["user", "post", ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
