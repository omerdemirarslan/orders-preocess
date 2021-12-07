from django.urls import path, include
from rest_framework import routers

from .views import (ProductsViewSet, RestaurantViewSet, CategoryViewSet)


router = routers.DefaultRouter()
router.register(r'products/get-products', ProductsViewSet)
router.register(r'categories/get-categories', CategoryViewSet)
router.register(r'partners/get-restaurants', RestaurantViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
