from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Categoria, Produto
from django.views.generic import ListView

def produto(request,slug=''):
    template='catalogo/product.html'
    try:
        produto = get_object_or_404(Produto,slug=slug)
        context = {
            'title':'Produto',
            'produto':produto
        }
    except Exception as e:
        print(e)
        context = {
            'title':'Produto',
            'produto':None
        }
    return render(request,template,context=context)


class ListaProduto(ListView):
    
    model = Produto
    template_name='catalogo/product_list.html'
    context_object_name = 'produtos'
    paginate_by=3
    
class CategoriaList(ListView):
    template_name='catalogo/lista_categoria.html'
    context_object_name='produtos'
    paginate_by=3
    
    def get_queryset(self):
        produtos =get_list_or_404(Produto,categoria__slug=self.kwargs['slug'])
        return produtos
    
    def get_context_data(self,**kwargs):
        context = super(CategoriaList, self).get_context_data(**kwargs)
        context['title']=get_object_or_404(Categoria,slug=self.kwargs['slug']).nome
        return context
    
    
def lista_por_categoria(request,slug=''):
    template='catalogo/lista_categoria.html'
    
    try:
        categoria = get_object_or_404(Categoria,slug=slug)
        produtos = get_list_or_404(Produto,categoria=categoria)
        context = {
            'title':categoria.nome,
            'produtos':produtos
        }
    except Exception as e:
        print(e)    
        context = {
            'title':'',
            'produtos':None
        }
    return render(request,template,context=context)