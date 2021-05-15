from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Categoria, Produto


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

def lista_produto(request):
    template='catalogo/product_list.html'
    context = {
        'title':'Lista de Produtos',
        'produtos':get_list_or_404(Produto)
    }
    return render(request,template,context=context)

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