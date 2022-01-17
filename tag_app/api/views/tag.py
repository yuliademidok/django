import itertools

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from publication_app.api.serializers.publications import PostSerializer
from tag_app.api.serializers.tag import TagSerializer, TagDetailSerializer
from tag_app.models import Tag


class TagViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    actions_serializers = {"retrieve": TagDetailSerializer, }

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)

    @action(methods=["get"], detail=True, serializer_class=PostSerializer)
    def posts(self, request, *args, **kwargs):
        tag = self.get_object()
        queryset = tag.post.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
