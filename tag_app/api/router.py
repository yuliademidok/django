from rest_framework import routers

from tag_app.api.views.tag import TagViewSet

api_router = routers.DefaultRouter()

api_router.register("tag", TagViewSet)
