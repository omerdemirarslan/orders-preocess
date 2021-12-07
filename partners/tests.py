from django.test import TestCase

from .models import Restaurant, Products, Category


class PartnersTestCase(TestCase):
    """ Test Case Class For Partners App """
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

    def test_get_restauran(self):
        """
        This Methods Get Control There Is An Objects In Restaurant Model
        :return:
        """
        restaurant = Restaurant.objects.get(name="Burger King")

        self.assertTrue(restaurant)
        self.assertEqual(restaurant.name, "Burger King")

    def test_get_category(self):
        """
        This Methods Get Control There Is An Objects In Category Model
        :return:
        """
        category = Category.objects.get(name="Fast Food")

        self.assertTrue(category)
        self.assertEqual(category.name, "Fast Food")

    def test_get_product(self):
        """
        This Methods Get Control There Is An Objects In Products Model
        :return:
        """
        products = Products.objects.get(name="Hamburger")

        self.assertTrue(products)
        self.assertEqual(products.name, "Hamburger")
