import redis

from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient

from utility.redis_helper.redis_client import RedisClient
from partners.models import Restaurant, Products, Category
from .models import Order


class OrdersTestCase(TestCase):
    """ Test Case Class For Orders App """
    def setUp(self):
        """
        This Method Create Objects For Restaurant, Category and Products
        :return:
        """
        restaurant = Restaurant(name="Burger King")
        restaurant.save()

        category = Category(name="Fast Food")
        category.save()

        products = Products(name="Hamburger", category=category, restaurants=restaurant)
        products.save()

    def test_create_order(self):
        """
        This Method Create Order
        :return:
        """
        new_order = Order(
            user_id=1,
            address="istiklal caddesi",
            amaunt="45.99",
            order=Products(name="Hamburger", restaurants_id=1)
        )

        self.assertTrue(new_order)
        self.assertEqual(new_order.address, "istiklal caddesi")


class OrdersApiTestCase(TestCase):
    """ Test Case Class For Orders API """
    def setUp(self):
        """
        This Method Create Objects For Restaurant, Category and Products
        :return:
        """
        self.factory = APIClient()

        restaurant = Restaurant(name="Burger King")
        restaurant.save()
        self.restaurant = Restaurant.objects.get(name="Burger King")

        category = Category(name="Fast Food")
        category.save()
        self.category = Category.objects.get(name="Fast Food")

        products = Products(name="Hamburger", category=category, restaurants=restaurant)
        products.save()
        self.products = Products.objects.get(name="Hamburger")

        new_user = User(username="testuser")
        new_user.save()

        self.new_user = User.objects.get(username="testuser")

    def test_order_create(self):
        """
        This Methot Create Order
        :return:
        """
        request = self.factory.post('/api/v1/order/create-order/', {
            "user": self.new_user.id,
            "address": "testadress",
            "amaunt": "45.99",
            "order": self.products.id,
            "quantity": "1",
            "status": "preparing"
        }, format='json')

        self.assertEqual(request.status_code, 201)

    def test_order_process(self):
        """
        This Methot Controls Order Process
        :return:
        """
        request = self.factory.post('/api/v1/order/get-order/', {
            "user": self.new_user.id,
            "address": "testadress",
            "order": self.products.id,
            "amaunt": "45.99",
            "quantity": "1",
            "status": "preparing"
        }, format='json')

        self.assertEqual(request.status_code, 400)

    def test_order_get(self):
        """
        This Methos Gets Orders
        :return:
        """
        request = self.factory.get('/api/v1/order/get-order/', format='json')

        self.assertEqual(request.status_code, 200)


class RedisTestCase(TestCase):
    """ This Case class For Redis """
    def test_redis(self):
        """ This Methot Connect Redis """
        connection = RedisClient().get_client()

        self.assertIsInstance(connection, redis.client.Redis)
