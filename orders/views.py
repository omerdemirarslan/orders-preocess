from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404

from rest_framework import viewsets, status
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response

from orders.models import Order
from orders.serializers import (SendOrderSerializer, OrderSerializer, GetOrderSerializer)

from utility.redis_helper.redis_client import RedisClient


class SendOrderViewSet(viewsets.ModelViewSet):
    """ Send Order To Pub/Sub """
    serializer_class = SendOrderSerializer
    queryset = Order.objects.none()

    def order_send_to_pub_sub(self, json_data: dict, channel_name: str):
        """
        This Method Send Order To Pub/Sub
        :param json_data:
        :param channel_name:
        :return:
        """
        RedisClient().publish_data_on_redis(
            json_data=json_data,
            channel_name=channel_name
        )

    def create(self, request, format=None, **kwargs):
        """
        This Method Create Order
        :param request:
        :param format:
        :param kwargs:
        :return:
        """
        serializer = SendOrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            self.order_send_to_pub_sub(
                json_data=serializer.data,
                channel_name="orders"
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = GetOrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('status',)

    def list(self, request, format=None, **kwargs):
        """
        This Method List Orders
        :param request:
        :param format:
        :param kwargs:
        :return:
        """
        serializer = GetOrderSerializer(self.filter_queryset(self.queryset), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, format=None, **kwargs):
        """
        This Method Update Order Status
        :param request:
        :param format:
        :param kwargs:
        :return:
        """
        try:
            pre_order = Order.objects.get(id=request.data.get('id'))
            pre_order.status = "Completed"
            pre_order.save()
        except Order.DoesNotExist:
            return Response({"Error": "Order does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"Success": "Order updated"}, status=status.HTTP_201_CREATED)

