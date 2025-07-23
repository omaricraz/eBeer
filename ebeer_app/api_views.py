from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product


def api_product_list(request):
    products = Product.objects.all()
    data = [
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'price': float(p.price),
            'image': p.image.url if p.image else None,
            'slug': p.slug,
        }
        for p in products
    ]
    return JsonResponse({'products': data})


def api_product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': float(product.price),
        'image': product.image.url if product.image else None,
        'slug': product.slug,
    }
    return JsonResponse(data)
