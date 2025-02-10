from django.urls import path
from product.views import shop, shop_detail

urlpatterns = [
    path('shop/', shop, name = 'shop'),
    path('shop/<int:pk>/', shop_detail, name = 'shop_detail'),

]
