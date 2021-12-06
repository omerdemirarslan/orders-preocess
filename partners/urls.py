from django.urls import path

from .views import (ProductsViewSet, RestaurantViewSet, CategoryViewSet)

app_name = 'api/v1'

urlpatterns = [
    path('products/get-products/', ProductsViewSet.as_view({'get': 'list'}), name='get_products'),
    path('categories/get-categories/', RestaurantViewSet.as_view({'get': 'list'}), name='get_categories'),
    path('restaurants/get-restaurants/', CategoryViewSet.as_view({'get': 'list'}), name='get_restaurants')
]
