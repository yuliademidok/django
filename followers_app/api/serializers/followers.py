from rest_framework import serializers

from ...models import Followers


class FollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        exclude = ("tag", )
        read_only_fields = ("follower_user", "created")

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="follower_user",
    )

    def validate(self, data):
        if data["follower_user"] == data["following_user"]:
            raise serializers.ValidationError("Following yourself is not allowed")
        return data


class FollowTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        exclude = ("following_user", )
        read_only_fields = ("follower_user", "created")

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="follower_user",
    )
