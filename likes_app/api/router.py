from rest_framework import routers

from likes_app.api.views.like import LikeViewSet

api_router = routers.DefaultRouter()

api_router.register("like", LikeViewSet)
