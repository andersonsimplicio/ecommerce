from django.urls import path,include
from .views import AddCartItemView

urlpatterns = [
   path('carrinho/adicionar/<slug:slug>',AddCartItemView.as_view(),name='create_caritem')
]