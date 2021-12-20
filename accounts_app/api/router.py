from rest_framework import routers

from accounts_app.api.views.users import UserViewSet

api_router = routers.DefaultRouter()

api_router.register("user", UserViewSet)
