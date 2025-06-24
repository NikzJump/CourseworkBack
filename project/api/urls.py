# Локальные URL адреса приложения

from django.urls import path
from . import views

urlpatterns = [
    path('products', views.get_products),
    path('signup', views.signup),
    path('login', views.login),
    path('cart/<int:category_id>/<int:pk>', views.add_cart),
    path('cart', views.get_cart),
    path('orders', views.get_order),
]
