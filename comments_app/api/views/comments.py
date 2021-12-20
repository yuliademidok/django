from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..serializers.comments import CommentSerializer
from ...models import Comment


class CommentViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    @action(methods=["get"], url_path='posts/(?P<post_id>[^/.]+)', detail=False)
    def post_id(self, request, post_id=None):
        queryset = Comment.objects.filter(post__id=post_id).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

