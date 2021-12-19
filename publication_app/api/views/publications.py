import django_filters
from django.db.models import F
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions

from publication_app.api.filters.publications import PostsFilterSet
from publication_app.api.serializers.publications import PostSerializer
from publication_app.models import Post


# class TestPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_authenticated:
#             return True
#         return False
#
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_authenticated:
#             return True
#         return False


class PostsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    # permission_classes = [TestPermission, ]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, ]
    ordering_fields = ["-create_date", ]

    filter_class = PostsFilterSet
    # filterset_fields = ("tags__name", )

    @action(methods=["get"], url_path='tags/(?P<tag_name>[^/.]+)', detail=False)
    def tag_name(self, request, tag_name=None):
        queryset = Post.objects.filter(tags__name=tag_name).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

