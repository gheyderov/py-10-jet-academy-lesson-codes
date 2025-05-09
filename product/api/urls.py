from django.urls import path
from product.api.views import categories, TagListAPIView, products, product_update, ProductListAPIView, ProductUpdateAPIView, SubscribeCreateAPIView, WishListAPIView, WishlistDestroyView


urlpatterns = [
    path('categories/', categories, name = 'categories'),
    path('tags/', TagListAPIView.as_view(), name = 'tags'),
    path('subscribers/', SubscribeCreateAPIView.as_view(), name = 'subscribers'),
    path('products/', ProductListAPIView.as_view(), name = 'products'),
    path('product/<int:pk>/', ProductUpdateAPIView.as_view(), name = 'product_update'),
    path('wishlist/', WishListAPIView.as_view(), name = 'wishlist_api'),
    path('wishlist/<int:pk>/', WishlistDestroyView.as_view(), name = 'wishlist_delete')
]