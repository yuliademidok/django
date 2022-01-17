from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions

from ..serializers.users import UserSerializer, UserCreationSerializer
from ...models import User


class IsAuthenticatedOrCreateOnly(permissions.IsAuthenticatedOrReadOnly):
    SAFE_METHODS = ('POST', )

    def has_permission(self, request, view):
        return bool(
            request.method in self.SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )


class UserViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrCreateOnly, ]

    actions_serializers = {"create": UserCreationSerializer, }

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)

    @action(methods=["get"], url_path='post/likes/(?P<post_id>[^/.]+)', detail=False)
    def post_likes(self, request, post_id=None):
        queryset = User.objects.filter(likes__post=post_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
