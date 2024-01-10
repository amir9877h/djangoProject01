from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render

from catalogue.models import Product, Category, ProductType, Brand


# Create your views here.
def products_list(request):
    # products = Product.objects.all()
    # # products = Product.objects.filter(is_active=True)
    # # products = Product.objects.exclude(is_active=False)
    #
    # categories = Category.objects.first()
    # # categories = Category.objects.get(id=1)
    # # products = Product.objects.filter(is_active=True, category=categories)
    # # products = Product.objects.filter(is_active=True, category_id=1)
    # # products = Product.objects.filter(is_active=True, category__name="Book")
    # # categories = Category.objects.last()
    #
    # brand = Brand.objects.filter(name='Brand01')
    #
    # product_type = ProductType.objects.filter(title="Book")
    # new_product = Product.objects.create(
    #     product_type=product_type,
    #     upc=7896555888,
    #     title="Product Created in Code!",
    #     description="",
    #     category=categories,
    #     brand=brand
    #
    # )

    # Product.objects.filter(is_active=True, category=categories).filter(brand= brand)

    products = Product.objects.select_related('category').all()

    context = "<br>".join([f"{product.title}, id => {product.upc}, category({product.category.name})" for product in products])
    return HttpResponse("Should Show all products: <br>" + "<h1>{}</h1>".format(context))


def products_detail(request, pk):
    # try:
    #     product = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     raise Http404("Product Not Found")
    querySet = Product.objects.filter(is_active=True).filter(Q(pk=pk) | Q(upc=pk))
    if querySet.exists():
        product = querySet.first()
    else:
        return HttpResponse("Product not found", status=404)
    return HttpResponse(f"<h1>Product Details => title: {product.title}</h1>")


def category_products(request, pk):
    try:
        category = Category.objects.prefetch_related('products').get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse("Category not found", status=404)
    # products = Product.objects.filter(category=category)

    products = category.products.all()

    product_ids = [1, 2, 3]
    # products = Product.objects.filter(id__in=product_ids)
    context = "<br>".join([f"{product.title}, id => {product.upc}" for product in products])
    return HttpResponse(f"Should Show all products with category({category}): <br>" + "<h1>{}</h1>".format(context))
