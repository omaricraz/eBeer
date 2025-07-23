from django.contrib import admin
from django.urls import path
from ebeer_app import views, api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('api/products/', api_views.api_product_list, name='api_product_list'),
    path('api/product/<slug:slug>/', api_views.api_product_detail, name='api_product_detail'),
]
