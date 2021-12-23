from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions

from publication_app.api.filters.publications import PostsFilterSet
from publication_app.api.serializers.publications import PostSerializer
from publication_app.models import Post

from tag_app.api.serializers.tag import TagDetailSerializer


class PostsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    # permission_classes = [TestPermission, ]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, ]
    ordering_fields = ["-create_date", ]

    filter_class = PostsFilterSet
    # filterset_fields = ("tags__name", )

    parser_classes = [MultiPartParser, JSONParser]

    @action(methods=["get"], url_path='tags/(?P<tag_name>[^/.]+)', detail=False)
    def tag_posts(self, request, tag_name=None):
        queryset = self.queryset.filter(tags__name=tag_name)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=True, name="post_tags", serializer_class=TagDetailSerializer)
    def post_tags(self, request, pk, *args, **kwargs):
        instance = self.get_queryset().get(pk=pk)
        serializer = self.get_serializer(instance.tags.all(), many=True)
        return Response(serializer.data)
