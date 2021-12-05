from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from partners.models import Restaurant, Products, Category


class Command(BaseCommand):
    help = u'Opens a connection to Redis and listens for messages, and then whenever it gets one, sends the message ' \
           u'onto a channel in the Django channel system'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def import_data(self):
        if not Restaurant.objects.all():
            restaurant = Restaurant(
                name="Bizim Büfe"
            )
            restaurant.save()

            category = Category(
                name="FastFood"
            )
            category.save()

            products = Products(
                name="Yengen",
                category=category,
                restaurants=restaurant
            )
            products.save()
            products = Products(
                name="Dilli Kaşarlı",
                category=category,
                restaurants=restaurant
            )
            products.save()
            products = Products(
                name="Goralı",
                category=category,
                restaurants=restaurant
            )
            products.save()

            restaurant = Restaurant(
                name="Harika Ev Yemekleri"
            )
            restaurant.save()

            category = Category(
                name="Ev Yemekleri"
            )
            category.save()

            products = Products(
                name="Mercimek Çorbası",
                category=category,
                restaurants=restaurant
            )
            products.save()
            products = Products(
                name="Pilav",
                category=category,
                restaurants=restaurant
            )
            products.save()
            products = Products(
                name="Kuru Fasülye",
                category=category,
                restaurants=restaurant
            )
            products.save()

            restaurant = Restaurant(
                name="Süper Dönerci"
            )
            restaurant.save()

            category = Category(
                name="Döner/Kebap"
            )
            category.save()
            products = Products(
                name="Döner",
                category=category,
                restaurants=restaurant
            )
            products.save()

            products = Products(
                name="İskender",
                category=category,
                restaurants=restaurant
            )
            products.save()
            products = Products(
                name="Etibol İskender",
                category=category,
                restaurants=restaurant
            )
            products.save()

            user = User(
                username="Uğur Özi",
                email="uozy@yspt.com"
            )
            user.save()

            user = User(
                username="Cenk Yaldız",
                email="cyaldiz@yspt.com"
            )
            user.save()

            user = User(
                username="Selin Simge",
                email="ssimge@yspt.com"
            )
            user.save()

    def handle(self, *args, **options):
        self.import_data()
