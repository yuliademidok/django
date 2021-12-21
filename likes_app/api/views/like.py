from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..serializers.like import LikeSerializer, LikeCommentSerializer
from ...models import Like


class LikeViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    @action(methods=["post"], url_path='comments', detail=False, serializer_class=LikeCommentSerializer)
    def create_comment_like(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

