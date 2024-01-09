from django.contrib import admin
from catalogue.models import Category, Brand, ProductType, Product, ProductAttribute
from django.contrib.admin import register


# from django.contrib.admin import register
# @register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('upc', 'title', 'is_active', 'product_type', 'category', 'brand')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('upc', 'title', 'category__name', 'brand__name')
    actions = ('active_all_products',)

    def active_all_products(self, request, queryset):
        pass


@register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_type', 'attribute_type')


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [ProductAttributeInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)  # => @register(Product) import => from django.contrib.admin import register
# admin.site.register(ProductType)
# admin.site.register(ProductAttribute, ProductAttributeAdmin) # => @register(ProductAttribute)
