from rest_framework.views import APIView
from rest_framework import viewsets

from partners.models import (Restaurant, Category, Products)
from .serializers import (ProductSerializer, CategorySerializer, RestaurantSerializer)


class ProductsViewSet(viewsets.ModelViewSet):
    """ Product View For All Product """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    """ Restaurant View For All Product """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ Category View For All Product """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer