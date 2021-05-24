from django.shortcuts import render,get_object_or_404
from django.views.generic import RedirectView
from .models import CarItem
from app.catalogo.models import Produto


class AddCartItemView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        produto = get_object_or_404(Produto,slug=self.kwargs['slug'])
        
        if self.request.session.session_key is None:
            self.request.session.save()
        
        cart_item = CarItem.objects.add_item(
            self.request.session.session_key,produto
        ) 
        return produto.get_absolute_url()
