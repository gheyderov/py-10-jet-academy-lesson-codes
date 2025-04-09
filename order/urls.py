from django.urls import path
from order.views import cart, wishlist, update_item

urlpatterns = [
    path('cart/', cart, name = 'cart'),
    path('update-item/', update_item, name = 'update_item'),
    path('wishlist/', wishlist, name = 'wishlist'),
]
