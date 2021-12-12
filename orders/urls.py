from django.urls import path, include
from rest_framework import routers

from .views import (SendOrderViewSet, ConfirmOrderViewSet, GetOrderViewSet)

router = routers.DefaultRouter()
router.register(r'orders/create-order', SendOrderViewSet, basename="create-order")
router.register(r'orders/confirm', ConfirmOrderViewSet, basename="confirm-order")
router.register(r'orders/get-orders', GetOrderViewSet, basename="get-orders")


urlpatterns = [
    path('api/v1/', include(router.urls))
]
