from rest_framework import routers

from ..api.views.users import UserViewSet

api_router = routers.DefaultRouter()

api_router.register("user", UserViewSet)
# api_router.register("user", UserCreateViewSet)
