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

    def validate(self, data):
        if data["user"] == data["post"].user:
            raise serializers.ValidationError("Liking own post is not allowed")
        return data


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ["user", "post", ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )

    def validate(self, data):
        if data["user"] == data["comment"].user:
            raise serializers.ValidationError("Liking own comment is not allowed")
        return data


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ["id", "post", "comment"]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user",
    )
