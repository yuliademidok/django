from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from subscriptions_app.api.serializers.subscriptions import SubscriptionSerializers
from subscriptions_app.models import Subscription


class SubscriptionViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = SubscriptionSerializers
    queryset = Subscription.objects.all()
