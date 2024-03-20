from django.urls import path
from .views import render_articulos, agregar_articulo, articleDetail

urlpatterns = [
    path('articulos/', render_articulos, name='articulos'),
    path('<int:id>', articleDetail, name = 'articleDetail'),
    path('agregar_articulo/', agregar_articulo, name = 'agregar_articulo'),
]
