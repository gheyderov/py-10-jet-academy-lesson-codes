from django.urls import path
from product.views import shop

urlpatterns = [
    path('shop/', shop, name = 'shop')
]
