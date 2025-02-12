from django.template import Library
register = Library()
from product.models import ProductCategory, Product


@register.simple_tag
def get_categories():
    return ProductCategory.objects.filter(parent = None)


@register.inclusion_tag('includes/recent-products.html')
def get_recent_products():
    recent_products = Product.objects.order_by('-created_at')[:3]
    return {
        'products' : recent_products
    }