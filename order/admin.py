from django.contrib import admin
from order.models import Basket, BasketItem, Wishlist

# Register your models here.


admin.site.register(Wishlist)
admin.site.register(Basket)
admin.site.register(BasketItem)