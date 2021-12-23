from rest_framework import routers
from ..api.views.followers import FollowUserViewSet, UnfollowUserViewSet

api_router = routers.DefaultRouter()
api_router.register("follow", FollowUserViewSet)
api_router.register("unfollow", UnfollowUserViewSet)
