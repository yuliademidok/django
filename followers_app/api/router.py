from rest_framework import routers
from ..api.views.followers import FollowUserViewSet, UnfollowUserViewSet, FollowTagViewSet

api_router = routers.DefaultRouter()
api_router.register("follow/user", FollowUserViewSet)
api_router.register("unfollow/user", UnfollowUserViewSet)
api_router.register("follow/tag", FollowTagViewSet)
