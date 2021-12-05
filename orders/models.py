from django.db import models
from django.contrib.auth.models import User

from partners.models import Products, Restaurant


# Create your models here.
class Order(models.Model):
    """ The Order Model For All Orders"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default="preparing")
    order = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
