from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.like import LikeSerializer
from ...models import Like


class LikeViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
