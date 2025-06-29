from django.shortcuts import render
from .models import FeaturedItem, Farm

def landing(request):
    featured_items = FeaturedItem.objects.all()
    top_farms = Farm.objects.order_by('-rating')[:6]
    context = {
        'featured_items': featured_items,
        'top_farms': top_farms,
    }
    return render(request, 'landing.html', context)


def demo(request):
    return render(request, 'index.html')