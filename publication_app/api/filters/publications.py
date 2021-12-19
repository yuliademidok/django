import django_filters
from django_filters.rest_framework import FilterSet

from publication_app.models import Post


class PostsFilterSet(FilterSet):
    tag = django_filters.Filter(field_name='tags__name')

    class Meta:
        model = Post
        fields = ['tag']
