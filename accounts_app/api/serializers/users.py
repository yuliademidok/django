from rest_framework import serializers

from likes_app.api.serializers.like import LikeSerializer
from ...models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "likes"]
        read_only_fields = ["id", ]

    likes = LikeSerializer(many=True, read_only=True)


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "date_joined"]
        read_only_fields = ["id", "date_joined"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
