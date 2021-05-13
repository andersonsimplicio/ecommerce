#config=utf-8
from django.shortcuts import render

def index(request):
    template='core/index.html'
    context = {
        'title':'Amazon'
    }
    return render(request,template,context=context)

def contato(request):
    template='core/contact.html'
    context = {
        'title':'Contato'
    }
    
    return render(request,template,context=context)

def produto(request):
    template='core/product.html'
    context = {
        'title':'Produto'
    }
    return render(request,template,context=context)

def lista_produto(request):
    template='core/product_list.html'
    context = {
        'title':'Lista de Produtos'
    }
    return render(request,template,context=context)