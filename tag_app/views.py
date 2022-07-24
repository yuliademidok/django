from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Prefetch
from django.shortcuts import render
from django.views import generic
from django.core.cache import cache

from publication_app.models import Post
from tag_app.models import Tag


class HashTagView(LoginRequiredMixin, generic.View):
    template_name = "tag_app/hashtag_posts.html"

    def get(self, request, hashtag, *args, **kwargs):
        # tag, created = Tag.objects.get_or_create(name=hashtag.lower())
        tag = Tag.objects.filter(name=hashtag.lower()).first()
        return render(request, self.template_name, {"tag": tag})


class HashTagCloudView(LoginRequiredMixin, generic.ListView):
    template_name = "tag_app/hashtag_cloud.html"

    def get(self, request, *args, **kwargs):
        tags = cache.get("tags")

        if not tags:
            tags = Tag.objects.annotate(count=Count('post')).prefetch_related(
                Prefetch(
                    'post',
                    queryset=Post.objects.only("id")
                )
            ).filter(count__gte=1)

            cache.set("tags", tags, 30)

        return render(request, self.template_name, {"tags": tags})
