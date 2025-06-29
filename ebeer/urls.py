
from django.contrib import admin
from django.urls import path, include
from ebeer_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.demo, name='demo')
]