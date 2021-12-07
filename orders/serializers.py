from django.contrib.auth.models import User, Group

from orders.models import Order
from rest_framework import serializers


class SendOrderSerializer(serializers.ModelSerializer):
    """ Send Order Serializer Class """

    class Meta:
        model = Order
        fields = ["id", "user", "address", "order", "amaount", "quantity", "status"]


class OrderSerializer(serializers.ModelSerializer):
    """ Order Serializer Class """

    class Meta:
        model = Order
        fields = ["user", "address", "order", "amaount", "quantity", "status"]

    def to_internal_value(self, data: dict) -> dict:
        """
        This Method Override The Data In The Incoming Request
        :param data:
        :return:
        """
        if not isinstance(data, dict):
            message = 'Incorrect type. Expected a string, but got %s'

            raise ValidationError(message % type(data).__name__)

        validated = {
            "id": data.get('id'),
            'user_id': data.get('user'),
            'address': data.get('address'),
            'status': "completed",
            'amaount': data.get('amaount'),
            'order_id': data.get('order'),
            'quantity': data.get('quantity'),


        }

        return validated


class GetOrderSerializer(serializers.ModelSerializer):
    """ Get Order Serializer Class """
    class Meta:
        model = Order
        fields = ["user", "address", "order", "amaount", "quantity", "status", "created_at"]
