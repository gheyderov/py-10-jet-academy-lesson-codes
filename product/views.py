from django.shortcuts import render, get_object_or_404
from product.models import Product, ProductCategory
from django.views.generic import DetailView


# Create your views here.

def shop(request):
    products = Product.objects.all() # queryset type = list
    categories = ProductCategory.objects.all()
    context = {
        'products' : products,
        'categories' : categories
        
    }
    return render(request, 'shop.html', context)


def shop_detail(request, pk):
    product = get_object_or_404(Product, id = pk)
    # product = Product.objects.get(id = pk)
    context = {
        'product' : product
    }
    return render(request, 'shop-detail.html', context)


# class ShopDetailView(DetailView):
#     template_name = 'shop-detail.html'
#     model = Product
    