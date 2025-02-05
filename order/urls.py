from django.urls import path
from order.views import cart, wishlist

urlpatterns = [
    path('cart/', cart, name = 'cart'),
    path('wishlist/', wishlist, name = 'wishlist'),
]
