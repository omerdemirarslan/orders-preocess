from django.urls import path, include
from rest_framework import routers

from .views import (SendOrderViewSet, OrderViewSet)

router = routers.DefaultRouter()
router.register(r'orders/create-order', SendOrderViewSet, basename="create-order")
router.register(r'orders/get-order', OrderViewSet, basename="get-order")

urlpatterns = [
    path('api/v1/', include(router.urls))
]
