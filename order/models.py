from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()
from product.models import Product
from account.models import UserAddress

# Create your models here.

class Wishlist(AbstractModel):

    user = models.ForeignKey(User, related_name='wishlists', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='wishlists', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    



class Basket(AbstractModel):

    user = models.ForeignKey(User, related_name='baskets', on_delete=models.CASCADE)
    # items = models.ManyToManyField(BasketItem)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
    def total_price(self):
        total_price = 0
        for item in self.items.all():
            total_price += item.price()
        return total_price
    

class BasketItem(AbstractModel):

    basket = models.ForeignKey(Basket, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField('quantity', default=1)

    def __str__(self):
        return self.product.title
    
    def price(self):
        return self.product.price * self.quantity
    
    class Meta:
        ordering = '-created_at',
    

class Order(AbstractModel):

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, related_name='orders', on_delete=models.CASCADE)
    useraddress = models.ForeignKey(UserAddress, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username