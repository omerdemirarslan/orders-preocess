from django.urls import path

from .views import (SendOrderViewSet, OrderViewSet)

app_name = 'api/v1/orders'

urlpatterns = [
    path('order/create-order/', SendOrderViewSet.as_view({'get': 'list'}), name='create-order'),
    path('order/get-order/', OrderViewSet.as_view({'get': 'list'}), name='order')
]
