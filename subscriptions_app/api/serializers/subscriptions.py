from rest_framework import serializers

from ...models import Subscription


class SubscriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
        read_only_fields = ("subscriber", )

    subscriber_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="subscriber",
    )
