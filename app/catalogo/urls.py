from django.urls import path,include
from .views import ListaProduto, CategoriaList, produto

urlpatterns = [
    path('produto/<slug:slug>/',produto,name='produto_details'),
    path('lista-de-produtos/',ListaProduto.as_view(),name='lista_produtos'),
    path('<slug:slug>',CategoriaList.as_view(),name='lista_categoria'),
]