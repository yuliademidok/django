from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.comments import CommentSerializer
from ...models import Comment


class CommentViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
