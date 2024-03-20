from django.urls import path, include

from products.views import productsDetail, renderProducts, agregar_producto

urlpatterns = [
    path('products/', renderProducts, name = 'products'),
    path('<int:id>/', productsDetail, name='productDetail'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
]