import django_filters
from django_filters.rest_framework import FilterSet

from followers_app.models import Followers
from publication_app.models import Post


class PostsByTagFilter(FilterSet):
    tag = django_filters.Filter(field_name='tags__name')

    class Meta:
        model = Post
        fields = ['tag']
