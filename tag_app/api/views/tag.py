from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from tag_app.api.serializers.tag import TagSerializer, TagDetailSerializer
from tag_app.models import Tag


class TagViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    actions_serializers = {"retrieve": TagDetailSerializer, }

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)
