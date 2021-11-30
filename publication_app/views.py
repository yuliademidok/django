import random

from django.shortcuts import render

from .models import Post


def main_page(request):
    # mock_posts = [{"title": random.randint(1, 10000), "text": "some text some text some text "} for _ in range(100)]
    posts = Post.objects.filter(is_public=True, ).order_by("-create_date", "-id").all()
    context = {
        "title": "Hi world",
        "posts": posts
    }
    return render(request, "mainpage.html", context)
