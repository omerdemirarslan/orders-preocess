from django.urls import path, include
from rest_framework import routers

from orders.urls import router as order_router
from partners.urls import router as partners_router

router = routers.DefaultRouter()
router.registry.extend(order_router.registry)
router.registry.extend(partners_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
