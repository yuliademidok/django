from itertools import chain

from django import template
from ..models import Menu

register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def menu(context):
    menu = Menu.objects.get(menu_label="main_menu")
    # profile = [{"url": context.request.user.username, "title": "My Profile"}]
    # return {"menu": chain(profile, menu.links.order_by("priority").all())}
    return {"menu": menu.links.order_by("priority").all()}


# @register.inclusion_tag("menu.html", takes_context=True)
# def login_menu(context):
#     if context.request.user.is_authenticated:
#         menu = [
#             {
#                 "url": context.request.user,
#                 "title": context.request.user
#             },
#             {
#                 "url": "/logout/",
#                 "title": "Logout"
#             },
#         ]
#         return {"menu": menu}
#     else:
#         menu = [
#             {
#                 "url": "/login/",
#                 "title": "Login"
#             },
#             {
#                 "url": "/registration/",
#                 "title": "Registration"
#             },
#         ]
#         return {"menu": menu}
