from rest_framework import serializers

from django.contrib.auth.models import User
from partners.models import Restaurant, Category, Products


class ProductSerializer(serializers.ModelSerializer):
    """ Product Serializer Class """
    class Meta:
        model = Products
        fields = ["name", "category", "restaurant"]


class RestaurantSerializer(serializers.ModelSerializer):
    """ Restaurant Serializer Class """
    class Meta:
        model = Restaurant
        fields = ["name", "is_active"]


class CategorySerializer(serializers.ModelSerializer):
    """ Category Serializer Class """
    class Meta:
        model = Category
        fields = ["name"]
