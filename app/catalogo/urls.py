from django.urls import path,include
from .views import lista_por_categoria, produto,lista_produto

urlpatterns = [
    path('produto/',produto,name='produto'),
    path('lista-de-produtos/',lista_produto,name='lista_produtos'),
    path('<slug:slug>',lista_por_categoria,name='lista_categoria'),
]