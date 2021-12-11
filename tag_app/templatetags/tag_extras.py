import re

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

register = template.Library()


def create_hashtag_link(tag):
    url = f"/explore/tags/{tag.lower()}/"
    return f'<a href="{url}">#{tag}</a>'


@register.filter
def hashtag_links(value):
    return mark_safe(re.sub(r"#(\w+)", lambda x: create_hashtag_link(x.group(1)), escape(value)))
