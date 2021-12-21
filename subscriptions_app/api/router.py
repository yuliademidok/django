from rest_framework import routers
from ..api.views.subscriptions import SubscriptionViewSet

api_router = routers.DefaultRouter()
api_router.register("subscription", SubscriptionViewSet)
