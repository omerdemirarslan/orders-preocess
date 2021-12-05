from rest_framework import serializers

from django.contrib.auth.models import User
from partners.models import Restaurant, Category, Products


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """ Product Serializer Class """

    class Meta:
        model = Products
        fields = '__all__'


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    """ Restaurant Serializer Class """

    class Meta:
        model = Restaurant
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """ Category Serializer Class """

    class Meta:
        model = Category
        fields = '__all__'
