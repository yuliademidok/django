from rest_framework import serializers

from ...models import Followers


class FollowerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = "__all__"
        read_only_fields = ("follower_user", "created")

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="follower_user",
    )

    def validate(self, data):
        if data["follower_user"] == data["following_user"]:
            raise serializers.ValidationError("Following yourself is not allowed")
        return data
