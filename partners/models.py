from django.db import models


class Restaurant(models.Model):
    """ The Restaurant Model For All Partners """
    name = models.CharField(max_length=255, verbose_name="partner_restaurant")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "partner_restaurant"


class Category(models.Model):
    """ The Category Models For Different Types"""
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Products(models.Model):
    """ The Product Model Related With Restaurants and Categories"""
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
