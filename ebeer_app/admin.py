from django.contrib import admin
from .models import Product, FeaturedItem, Farm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

admin.site.register(FeaturedItem)
admin.site.register(Farm)
