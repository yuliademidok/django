from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..serializers.users import UserSerializer
from ...models import User


class UserViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=["get"], url_path='post/likes/(?P<post_id>[^/.]+)', detail=False)
    def post_likes(self, request, post_id=None):
        queryset = User.objects.filter(likes__post=post_id).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
