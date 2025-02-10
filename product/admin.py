from django.contrib import admin
from product.models import ProductCategory, Product, ProductImage, ProductReview, ProductTag
from product.forms import ProductAdminForm
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price', 'quantity', 'get_tags']
    list_display_links = ['id', 'title']
    list_editable = ['category', 'quantity']
    list_filter = ['category']
    list_per_page = 6
    search_fields = ['title', 'category__title']
    inlines = [ProductImageInline]
    form = ProductAdminForm

    def get_tags(self, obj):
        tags = []
        for tag in obj.tags.all():
            tags.append(tag.title)
        return tags
    



admin.site.register(ProductCategory)
admin.site.register(ProductTag)
admin.site.register(ProductReview)
admin.site.register(ProductImage)