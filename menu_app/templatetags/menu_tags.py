from itertools import chain

from django import template

from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def menu(context):
    try:
        menu = Menu.objects.get(menu_label="main_menu")
    except Menu.DoesNotExist as exc:
        menu = Menu.objects.create(menu_label="main_menu")
        MenuItem.objects.create(menu=menu, title="logout", url="/logout/", priority="40")
        MenuItem.objects.create(menu=menu, title="main_page", url="/", priority="10")
        menu = Menu.objects.get(menu_label="main_menu")

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
