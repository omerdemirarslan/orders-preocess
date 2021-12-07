from django.urls import path

from .views import (SendOrderViewSet, OrderViewSet)

app_name = 'api/v1/orders'

urlpatterns = [
    path('create-order/', SendOrderViewSet, name='create-order'),
    path('get-order/', OrderViewSet, name='order')
]
