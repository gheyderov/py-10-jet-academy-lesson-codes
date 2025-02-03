from django.contrib import admin
from product.models import ProductCategory, Product, ProductImage

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)