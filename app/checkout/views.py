from django.shortcuts import render,get_object_or_404
from django.urls.base import reverse
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView

from .models import CarItem
from app.catalogo.models import Produto
from django.forms import modelformset_factory 

class AddCartItemView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        produto = get_object_or_404(Produto,slug=self.kwargs['slug'])
        
        if self.request.session.session_key is None:
            self.request.session.save()
        
        cart_item,created = CarItem.objects.add_item(
            self.request.session.session_key,produto
        ) 
        if created:
            print('Produto adcionado com sucesso')
        else:
            print('Produto atualizado com sucesso') 
        
        return reverse('checkout:cartitem')




class CarItemView(TemplateView):
    template_name="checkout/cart.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context
    
    
    def get_formset(self,clear=False):
        carItemFormset = modelformset_factory(
            CarItem,
            fields=('quantidade',),
            can_delete=True,
            extra=0
        )
        _chave=self.request.session.session_key
        if self.request.session.session_key:
            if clear:
                formset = carItemFormset(
                    queryset=CarItem.objects.filter(chave=_chave))
            else:
                formset = carItemFormset(
                    queryset=CarItem.objects.filter(chave=_chave),
                    data=self.request.POST or None
                )
        else:
            formset=carItemFormset(
                queryset=CarItem.objects.none())
        return formset
    
    def post(self,request,*args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            message='Carrinho atualizado'
            context['msg'] =message
            formset = self.get_formset(clear=True)
        
        return self.render_to_response(context=context)