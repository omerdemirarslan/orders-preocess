from django.contrib.auth.models import User

from rest_framework import serializers
from orders.models import Order


class SendOrderSerializer(serializers.ModelSerializer):
    """ Send Order Serializer Class """

    class Meta:
        model = Order
        fields = ["id", "user", "address", "order", "quantity", "status", "created_at", "updated_at"]


class OrderSerializer(serializers.ModelSerializer):
    """ Order Serializer Class """

    class Meta:
        model = Order
        fields = ["user", "address", "order", "quantity", "status"]

    def to_internal_value(self, data):
        validated = {
            "id": data.get("id"),
            "user_id": data.get("user"),
            "address": data.get("address"),
            "order_id": data.get("order"),
            "quantity": data.get("quantity"),
            "status": "processed",

        }

        return validated


class GetOrderSerializer(serializers.ModelSerializer):
    """ Get Order Serializer """

    class Meta:
        model = Order
        fields = ["user", "address", "order", "quantity", "status", "created_at", "updated_at"]