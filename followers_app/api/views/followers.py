from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from followers_app.api.serializers.followers import FollowerSerializers
from followers_app.models import Followers


class FollowUserViewSet(GenericViewSet, CreateModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FollowerSerializers
    queryset = Followers.objects.all()


class UnfollowUserViewSet(GenericViewSet, DestroyModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FollowerSerializers
    queryset = Followers.objects.all()
