#config=utf-8
from django.shortcuts import render,get_list_or_404
from app.catalogo.models import Categoria,Produto

def index(request):
    template='core/index.html'
    context = {
        'title':'Amazon',
    }
    return render(request,template,context=context)

def contato(request):
    template='core/contact.html'
    context = {
        'title':'Contato'
    }
    
    return render(request,template,context=context)


