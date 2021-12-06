from django.urls import path

from .views import (SendOrderViewSet, OrderViewSet)

app_name = 'api/v1/order'

urlpatterns = [
    path('create-order/', SendOrderViewSet.as_view({'get': 'list'}), name='create-order'),
    path('get-order/', OrderViewSet.as_view({'get': 'list'}), name='order')
]
