from django.urls import path,include
from .views import AddCartItemView,CarItemView

urlpatterns = [
   path('carrinho/adicionar/<slug:slug>',AddCartItemView.as_view(),name='create_caritem'),
   path('carrinho/',CarItemView.as_view(),name='cartitem'),
]